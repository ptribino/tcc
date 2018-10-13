from django.urls import include, path
from . import views

app_name='armario'
urlpatterns = [
    path('', views.armarionew, name='armarionew'),
   # path('<int:pk>', views.details, name='details'),
]