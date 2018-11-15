from django import forms


# Watson dependencies
import json
from watson_developer_cloud import AssistantV1

# Getting APIKEY variable from settings
#APIKEY = getattr(settings, "APIKEY", None)


assistant = AssistantV1(
     version='2018-09-20',
     username='d662d4ba-9e5d-4631-b94b-23446011f580',
     password='HlfulHf7UuJQ',
     url='https://gateway.watsonplatform.net/conversation/api/v1/workspaces/d44da73a-4abb-4cd0-9ab1-803488fdec1f/message'
 )

# class CommentForm(forms.Form):
#     comment = forms.CharField(
#         label="Comment", widget=forms.Textarea(attrs={'rows': 10}), required=True)

     # def ask_watson(self):
     #     text = self.cleaned_data['comment']
     #     combined_operations = ['doc-sentiment']
     #     watson_assistant.message()
     #     #return watson_assistant.combined(text=text, extract=combined_operations)
     #     return self

response = assistant.message(
    workspace_id='d44da73a-4abb-4cd0-9ab1-803488fdec1f',
    input={
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))