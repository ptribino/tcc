from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
from django.views.generic.edit import FormView
from .forms import ChatForm


class ChatView(FormView):
    template_name = "watson_app/chat.html"
    form_class = ChatForm
    success_url = "watson_app/Stella.html"

    def index(request):
        return render(request, 'watson_app/chat.html')


    # def form_valid(self, form):
    #     serialized_json = json.dumps(form.ChatForm(), sort_keys=True, indent=4)
    #     return HttpResponse(serialized_json, content_type="application/json")
