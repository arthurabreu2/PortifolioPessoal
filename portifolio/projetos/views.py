from django.shortcuts import render


def index(request):
    return render(request, 'projetos/index.html')

def projetos(request):
    return render(request, 'projetos/projetos.html')

def projeto_detalhes(request):
    return render(request, 'projetos/projeto_detalhes.html')
