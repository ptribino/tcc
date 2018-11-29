from django.urls import path
#from .views import ListaItensView
from .views import ArmarioCreateView
from .views import ArmarioListView
from .views import ArmarioUpdateView
from .views import ArmarioDeleteView


app_name = 'armario'

urlpatterns = [
    # GET /itens/listar
    # path('itens/lista_itens/<pk>', ListaItensView.as_view(), name="lista_itens"),
    # GET /armario/cadastrar
    path('armario/cadastrar/', ArmarioCreateView.as_view(), name="armario_cadastrar"),
    # GET /armario
    path('armarios/', ArmarioListView.as_view(), name="lista_armarios"),

    # GET/POST /armario/{pk}
    path('armarios/<pk>', ArmarioUpdateView.as_view(), name="atualiza_armarios"),

    # GET/POST /armarios/excluir/{pk}
    path('armarios/excluir/<pk>', ArmarioDeleteView.as_view(), name="deleta_armario"),

]
