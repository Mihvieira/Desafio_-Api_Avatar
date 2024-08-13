# Objetivos
Consumir uma API de Avatar para receber as personagens e suas características em desafios propostos durante 7 dias.
Deverá ser criada uma tela básica exibindo os dados e com paginação. No processo, também utilizaremos o Bootstrap junto ao Django.

# Dia 1/7 - Desafio
Criar o código Python para executar uma requisição HTTP do tipo GET usando o módulo requests.
Executar a requisição e pegar a resposta (o JSON).
Imprimir o corpo da resposta através de um print.

## Código:
```
import requests
import pandas as pd

url = "https://last-airbender-api.fly.dev/api/v1/characters"
requisicao = requests.get(url)
informacoes = requisicao.json()

tabela = pd.DataFrame(informacoes)
print(tabela)
```
## Resultado

![resultadoApi](https://github.com/user-attachments/assets/6c57fe63-9367-4998-a564-8c93ef3098fd)

