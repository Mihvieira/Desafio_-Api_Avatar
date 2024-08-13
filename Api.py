import requests
import pandas as pd

url = "https://last-airbender-api.fly.dev/api/v1/characters"
requisicao = requests.get(url)
informacoes = requisicao.json()

tabela = pd.DataFrame(informacoes)
print(tabela)