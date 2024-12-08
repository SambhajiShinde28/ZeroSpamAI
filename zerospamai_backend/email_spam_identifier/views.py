from django.shortcuts import render
from django.http import HttpResponse


def SpamPredict(req):
    return HttpResponse("This is Email Classifier.")
