from django.db import models
from django.contrib.auth.models import User
#from .models import Itens


class ArmarioManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(created_at__icontains=query)
        )

objects = ArmarioManager()


class Armario(models.Model):
    name = models.CharField('Nome', max_length=50, blank=False)
    slug = models.SlugField('Atalho')
    descricao = models.CharField('Descrição', max_length=100, blank=True)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.PROTECT, related_name='user')

    objetos = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Armário'
        verbose_name_plural = 'Armários'
       # ordering = ['name']

class ArmarioItem(models.Model):

    armario = models.ForeignKey(Armario, blank=False, on_delete=models.CASCADE)
    itens = models.ForeignKey('itens.Itens', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.armario.name + '_' + self.itens.name

