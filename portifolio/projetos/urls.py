from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("projetos", views.projetos, name='projetos'),
    path("projeto_detalhes/<int:projetoid>", views.projeto_detalhes, name='projeto_detalhes')
]
