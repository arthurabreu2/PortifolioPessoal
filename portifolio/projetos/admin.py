from django.contrib import admin
from .models import Projeto

# Register your models here.
class ListandoProjetos(admin.ModelAdmin):
    """
    Classe para mudar o layout da listagem de projetos na área de administração
    """
    list_display = ("id", 'nome_projeto', 'linguagem')
    list_display_links = ('id', 'nome_projeto')
    search_fields = ('nome_projeto', 'descricao_projeto')
    list_filter = ('cliente',)
    list_per_page = 2


admin.site.register(Projeto, ListandoProjetos)