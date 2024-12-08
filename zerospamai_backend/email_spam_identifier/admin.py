from django.contrib import admin
from .models import EmailSpamModel


@admin.register(EmailSpamModel)
class EmailSpamAdmin(admin.ModelAdmin):
    list_display=('UserMessage', 'SpamProbability', 'NotSpamProbability', 'ModelPrediction', 'Category',)
    

