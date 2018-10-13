from django.contrib import admin

from .models import Itens

class ItemAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'cor', 'categoria','image']
    search_fields = ['name', 'slug', 'cor']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Itens, ItemAdmin)


