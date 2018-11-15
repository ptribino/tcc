from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Itens

class ItemAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug','image','categoria', 'cor', 'itens_image']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields=['itens_image']

    def itens_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width = obj.image.width,
            height=obj.image.height,
            )
        )

admin.site.register(Itens,ItemAdmin)
