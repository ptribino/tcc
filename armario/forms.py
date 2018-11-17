from django import forms
from .models import Armario



class InsereArmarioForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Armario

        # Campos que estarão no form
        fields = [
            'name',
            'descricao'
        ]
