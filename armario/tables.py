import django_tables2 as tables
from django_tables2.utils import A
from .models import Armario

class ArmarioTable(tables.Table):
    name = tables.LinkColumn('Nome', args=[A('pk')])
    descricao = tables.LinkColumn('Descrição', args=[A('pk')])
    created_at = tables.LinkColumn('Criado em', args=[A('pk')])
    updated_at = tables.LinkColumn('Atualizado em', args=[A('pk')])

class Meta:
    model = Armario
    fields = ('name', 'descricao', 'created_at', 'updated_at')