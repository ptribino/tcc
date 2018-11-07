from django.db import models

class ArmarioManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(created_at__icontains=query)
        )

objects = ArmarioManager()

class Armario(models.Model):

    name= models.CharField(max_length=50, blank=False)
    slug = models.SlugField('Atalho')
    descricao = models.CharField(max_length=100, blank=True)
    created_at = models.DateField('Criado em', auto_now_add=False)
    updated_at = models.DateField('Atualizado em',auto_now=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Armário'
        verbose_name_plural = 'Armários'
        ordering = ['name']