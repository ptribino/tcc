from django.contrib import admin

from .models import Itens

class ItemAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug','image','categoria', 'cor']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Itens,ItemAdmin)
