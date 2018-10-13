from django.contrib import admin
from .models import Armario

class ArmarioAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'descricao', 'created_at']#,'updated_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Armario, ArmarioAdmin)
