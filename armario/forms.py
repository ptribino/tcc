from .models import Armario
from django import forms


class InsereArmarioForm(forms.ModelForm):
    name = forms.CharField(
        label='Nome armário',
        required=True,
    )

    descricao = forms.CharField(
        label='Descrição',
        required=False,
        widget=forms.Textarea
    )

    created_at = forms.DateField(
        label='Criado em',
        required=False,
        widget=forms.DateField
    )


class Meta:
    model = Armario

    fields = [
        'nome',
        'descricao',
        'created_at',
    ]
