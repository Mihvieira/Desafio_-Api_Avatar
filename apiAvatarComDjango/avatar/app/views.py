from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import requests
import json


def index(request):
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    requisicao = requests.get(url)
    informacoes = requisicao.json()
    dicionario = {}
    for item, valor in enumerate(informacoes):
        dicionario[item]=valor
    
    context = {
        'personagens': dicionario
    }
    return render(request, "index.html", context)


def transformContext(informacoes):   
    contexto = {
        'nome' : informacoes['name'],
        'aliados': informacoes['allies'],
        'inimigos': informacoes['enemies'],
        'fotoUrl': informacoes['photoUrl'],
        'afiliacao': informacoes['affiliation']
    }