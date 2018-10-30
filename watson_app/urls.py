from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views

app_name='watson_app'
urlpatterns = [
    re_path(r'^watson/', views.CommentView, name='comment'),
    #path('watson_app/', views.form_valid, name='comment'),
]