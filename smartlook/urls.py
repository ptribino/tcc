from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('itens/', include('itens.urls', namespace='itens')),
    path('armario/', include('armario.urls', namespace='armario')),
    #path('estilo', include('estilo.urls', namespace='estilo')),
    path('conta', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('watson/', include('watson_app.urls', namespace='comment')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)