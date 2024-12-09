from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import EmailSpamModel

import pandas as pd
import joblib
import numpy as np
import os
from django.conf import settings
import sklearn


model_path=os.path.join(settings.BASE_DIR,'ml-model/EmailSpam_Model.pkl')
vectorizer_path=os.path.join(settings.BASE_DIR,'ml-model/Message_Vectorizer.pkl')

MultinomialNB_model = joblib.load(model_path)
vectorize = joblib.load(vectorizer_path)


@csrf_exempt
def SpamPredict(req):
    
    if req.method == "POST":

        data=json.load(req)

        if data["email"] != "":
             
            encoaded_data=vectorize.transform([data["email"]])
            model_prediction=MultinomialNB_model.predict(encoaded_data)
            model_probability=MultinomialNB_model.predict_proba(encoaded_data)

            Spam_Percentage=round(model_probability[0][1]*100,2)
            NotSpam_Percentage=round(model_probability[0][0]*100,2)

            Category="Spam" if model_prediction[0]==1 else "NotSpam"

            savingData = EmailSpamModel(UserMessage=data["email"], SpamProbability=Spam_Percentage, NotSpamProbability=NotSpam_Percentage, ModelPrediction=model_prediction[0], Category=Category)
            savingData.save()
            
            return JsonResponse({"Message":"prediction","Category":Category,"SpamPercentage":Spam_Percentage,"NotSpamPercentage":NotSpam_Percentage})
        
        else:
            return JsonResponse({"Message":"EmailEmpty"})
    
    else:
        return JsonResponse({"Message":"wrong request"})
    
