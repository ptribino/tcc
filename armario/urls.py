from django.urls import path
from .views import ArmarioCreateView, ArmarioListView, ArmarioUpdateView, ArmarioDeleteView

app_name = 'armario'

urlpatterns = [
    # GET /
    # path('', IndexTemplateView.as_view(), name="index"),

    # GET /armario/cadastrar
    path('armario/cadastrar/', ArmarioCreateView.as_view(), {'template_name': 'armario/cadastra.html'}, name="armario_cadastrar"),

    # GET /armario
    path('armarios/', ArmarioListView.as_view(), name="lista_armarios"),

    # GET/POST /armario/{pk}
    path('armarios/<pk>', ArmarioUpdateView.as_view(), name="atualiza_armarios"),

    # GET/POST /armarios/excluir/{pk}
    path('armarios/excluir/<pk>', ArmarioDeleteView.as_view(), name="deleta_armario"),
]
