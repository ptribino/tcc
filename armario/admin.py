from django.contrib import admin
from .models import Armario
from .models import ArmarioItem

class ItemArmarioInLine(admin.TabularInline):
    model=ArmarioItem

class ArmarioAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'descricao', 'created_at','updated_at', 'user']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ItemArmarioInLine]


class ArmarioItemAdmin(admin.ModelAdmin):

    list_display = ['armario.name', 'itens.name', 'itens.image']

admin.site.register(Armario, ArmarioAdmin)
admin.site.register(ArmarioItem)


