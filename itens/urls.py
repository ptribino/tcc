from django.urls import include, path, re_path
from . import views

app_name='itens'
urlpatterns = [
    path('', views.index, name='index'),
   # path('<int:pk>', views.details, name='details'),
     re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),

]