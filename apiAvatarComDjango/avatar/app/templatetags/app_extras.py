from django import template
from django.template.defaulttags import register
from django.template.defaultfilters import stringfilter
from googletrans import Translator

register = template.Library()
tradutor = Translator()

@register.filter(name="get_item")
def get_item(dictionary, key):
    if key == 'photoUrl':
        return dictionary.get(key)
    else:
        dado = dictionary.get(key)
        return traduzir_item(dado)


@register.filter(name='traduzir_item')
def traduzir_item(valor):
    try:
        if len(valor) == 0:
            return 0
        
        elif valor == 'Bum-Ju':
            return valor
        
        elif type(valor) is list:
            lista = []
            for i in valor:
                if len(i) > 5:
                    traduzir = tradutor.translate(i,dest= 'pt').text
                    lista.append(traduzir.title())
                else:
                    lista.append(i.title())
            
            if len(lista) > 1:
                return ', '.join(str(element) for element in lista)
            else:
                return lista[0]
        
        elif len(valor) > 5:
            traduzir = tradutor.translate(valor,dest= 'pt').text
            return traduzir.title()
        
        else:
            return valor
             
    except:
        return valor

