
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('entrar/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('sair/', auth_views.logout, {'next_page': 'core:home'}, name='logout'),
    path('cadastre-se/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar-senha/', views.edit_password, name='edit_password'),
    path('editar/', views.edit, name='edit'),
]