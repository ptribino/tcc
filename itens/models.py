from django.db import models

# CATEGORIA_CHOICES=[
#     ('acessorios', 'Acessórios'),
#     ('bermudas', 'Bermudas'),
#     ('blusas', 'Blusas'),
#     ('calcados', 'Calçados'),
#     ('casacos', 'Casacos'),
#     ('praia', 'Praia'),
#     ('saias', 'Saias'),
#     ('vestidos', 'Vestidos'),
# ]

class ItenManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(cor__icontains=query)
        )



class Itens(models.Model):

    name = models.CharField('Nome:', max_length=100)
    slug = models.SlugField('Atalho:')
    cor = models.CharField('Cor:', max_length= 20, blank=True)
    #categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Acessórios')
    categoria = models.CharField('Categoria',max_length=20, null=True,blank=False)
    image = models.ImageField(
        upload_to='', verbose_name='Imagem:', null=True, blank=True
    )

    objects = ItenManager()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('itens:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['name']