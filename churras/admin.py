from django.contrib import admin
from .models import Prato
# Register your models here.

class ListandoPratos(admin.ModelAdmin):
    list_display = ('id', 'nome_prato', 'categoria', 'tempo_preparo', 'publicado')
    list_editable = ('publicado',)
    list_display_links = ('id', 'nome_prato')
    search_fields = ('nome_prato', 'categoria')
    list_filter = ('categoria',)
    list_per_page = 10
    ordering = ('id',)
    


admin.site.register(Prato, ListandoPratos)