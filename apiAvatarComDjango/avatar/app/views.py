from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


def index(request):
    pagina = request.GET.get('page', 1)
    quantidade_por_pagina = 10
    url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage={quantidade_por_pagina}&page={pagina}'
    requisicao = requests.get(url)
    dados = requisicao.json()
    dicionario = {}
    for item, valor in enumerate(dados):
        dicionario[item] = valor    
    
    context = {
        'personagens' : dicionario,
        'chaves' : list(dicionario[0].keys())
    }
        
    return render(request, "index.html", context)
