from django import forms
from django.http import HttpResponse
from django.conf import settings

# Watson dependencies
import json
from os.path import join, dirname
from watson_developer_cloud import AssistantV1

# Getting APIKEY variable from settings
#APIKEY = getattr(settings, "APIKEY", None)

# Watson authentication
watson_assistant = AssistantV1(
     version='{2018-09-20}',
     username='{d662d4ba-9e5d-4631-b94b-23446011f580}',
     password='{HlfulHf7UuJQ}',
     url='{https://gateway.watsonplatform.net/conversation/api}'
 )

class CommentForm(forms.Form):
    comment = forms.CharField(
        label="Comment", widget=forms.Textarea(attrs={'rows': 10}), required=True)

    def ask_watson(self):
        text = self.cleaned_data['comment']
        combined_operations = ['doc-sentiment']
        return watson_assistant.combined(text=text, extract=combined_operations)