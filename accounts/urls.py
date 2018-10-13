
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('entrar/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    #path('sair/', views.logout, name='logout'),
    path('cadastre-se/', views.register, name='register'),

]