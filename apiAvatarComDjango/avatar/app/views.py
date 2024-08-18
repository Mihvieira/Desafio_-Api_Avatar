from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import requests
import json
from googletrans import Translator


def transformarDados(informacoes):
    personagens = {}
    tradutor = Translator()
    
    for item, valor in enumerate(informacoes):
        for chave in valor:
            if chave == '_id':
                None
            else:
                traducaoColunas = tradutor.translate(chave,dest= 'pt').text
                dado = valor.get(chave) #retorna os dados da chave
                
                if type(dado) == list:
                    listaDados = []
                    for i in dado:
                        traducaoDados = tradutor.translate(i,dest= 'pt').text
                        listaDados.append(traducaoDados)
                    personagens[traducaoColunas]=listaDados
                else:
                    traducaoDados = tradutor.translate(dado,dest= 'pt').text
                    personagens[traducaoColunas]=traducaoDados
    
    return personagens

def index(request):
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
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