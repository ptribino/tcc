from django.forms import ModelForm
from armario.models import Armario


class ArmarioForm(ModelForm):
    class Meta:
        model = Armario

    fields = ['name', 'descricao','created_at']#,'updated_at']

