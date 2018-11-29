from django import forms
from .models import Armario
#from .models import ArmarioItem


class InsereArmarioForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     super(InsereArmarioForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     instance = super(InsereArmarioForm, self).save(commit=False)
    #     instance.user = self.user
    #     return super(InsereArmarioForm, self).save(commit=commit)

    class Meta:
        # Modelo base
        model = Armario

        # Campos que estarão no form
        fields = [
            'name',
            'descricao'
        ]

        exclude = [
            'created_at,'
            'user'
        ]


# class ArmarioItemForm(forms.ModelForm):
#     class Meta:
#         model = ArmarioItem
#
# fields = "__all__"

