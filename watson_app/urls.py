from django.urls import  path
from . import views

app_name='watson_app'

urlpatterns = [
    path('watson/', views.ChatView, name='chat'),
    #path('watson_app/', views.form_valid, name='comment'),
]


