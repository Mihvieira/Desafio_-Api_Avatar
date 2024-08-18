from django import template
from django.template.defaulttags import register
from django.template.defaultfilters import stringfilter
from googletrans import Translator

register = template.Library()
tradutor = Translator()

@register.filter(name="get_item")
def get_item(dictionary, key):
    dado = dictionary.get(key)
    return traduzir_item(dado)

# TODO avaliar adição de exceções 
@register.filter(name='traduzir_item')
def traduzir_item(valor):
    try:
        if type(valor) is list:
            lista = []
            for i in valor:
                traduzir = tradutor.translate(i,dest= 'pt').text
                lista.append(traduzir)
            return lista
        else:
            traduzir = tradutor.translate(valor,dest= 'pt').text
            return traduzir            
    except:
        return valor

