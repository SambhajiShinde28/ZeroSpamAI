from django.db import models


class EmailSpamModel(models.Model):
    UserMessage=models.TextField(default="None")
    SpamProbability=models.IntegerField(default=0)
    NotSpamProbability=models.IntegerField(default=0)
    ModelPrediction=models.CharField(max_length=200,default="None")
    Category=models.CharField(max_length=200,default="None")

