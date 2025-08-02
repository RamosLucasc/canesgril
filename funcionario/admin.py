from django.contrib import admin
from .models import Funcionario

class ListandoFuncionados(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
# Register your models here.
admin.site.register(Funcionario, ListandoFuncionados)
