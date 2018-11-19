from django import forms

class ChatForm(forms.Form):
      comment = forms.CharField(
        label="Comment", widget=forms.Textarea(attrs={'rows': 10}), required=True)


     # def ask_watson(self):
     #     text = self.cleaned_data['comment']
     #     combined_operations = ['doc-sentiment']
     #     assistant.message()
     #     return assistant.combined(text=text, extract=combined_operations)
     #     return self

