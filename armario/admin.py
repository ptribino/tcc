from django.contrib import admin
from .models import Armario


class ArmarioAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'descricao', 'created_at','updated_at', 'user']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ArmarioItemAdmin(admin.ModelAdmin):

    list_display = ['armario.name', 'itens.name']

admin.site.register(Armario, ArmarioAdmin)


