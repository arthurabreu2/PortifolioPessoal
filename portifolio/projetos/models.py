from datetime import datetime
from django.db import models


# Create your models here.
class Projeto(models.Model):
    """
    Classe para modelar e criar um banco de dados para meu app
    """
    nome_projeto = models.CharField(max_length=200)
    descricao_projeto = models.TextField()
    cliente = models.CharField(max_length=100)
    data_conclusao = models.DateTimeField(default=datetime.now, blank=True)
    website = models.CharField(max_length=200)
    linguagem = models.CharField(max_length=80)
    tags_projetos = models.TextField()
    detalhes_projetos = models.TextField()