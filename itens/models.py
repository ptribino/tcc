from django.db import models

class Categoria(models.Model):
    name_categoria = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name_categoria

class Cor(models.Model):
    cor_item = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.cor_item

class ItenManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query)  | \
            #models.Q(cor__icontains=query)  | \
            models.Q(categoria__icontains=query)
        )

class Itens(models.Model):

    name = models.CharField('Nome:', max_length=100)
    slug = models.SlugField('Atalho:')
    categoria = models.ForeignKey('Categoria', related_name='itens', on_delete=models.CASCADE)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='itens_imagens', verbose_name='Imagem:', null=True, blank=True
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