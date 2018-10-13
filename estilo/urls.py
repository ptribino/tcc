from django.urls import path
from estilo import views

app_name = 'estilo'
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/',views.contact, name='contact'),
]
