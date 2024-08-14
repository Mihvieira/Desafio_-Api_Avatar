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


# Dia 2/7 - Desafio
"[...]fazer a tradução de alguns atributos da API, como: name e affiliation. [...]Recomendamos tentar com a biblioteca Googletrans.
[...]Após criar a função, faça um print para ver como estão os nomes traduzidos."

## Código

```
import requests
import pandas as pd
from googletrans import Translator


def traduzirColunas(lista):
    tradutor = Translator()
    index = 1
    for i in lista[1:]:
        traducao = tradutor.translate(i, 'pt')
        tabela.rename({lista[index]: traducao.text}, axis='columns', inplace=True)
        index += 1

def traduzirLinhas(lista):
    tradutor = Translator()
    novaLista = []
    index = 1
    for i in lista:
        traducao = tradutor.translate(i, 'pt')
        novaLista.append(traducao.text)
    
    tabela['afiliação'].replace(lista, novaLista, inplace=True)

url = "https://last-airbender-api.fly.dev/api/v1/characters"
requisicao = requests.get(url)
informacoes = requisicao.json()

tabela = pd.DataFrame(informacoes)
nomesColunas = tabela.columns.tolist()
traduzirColunas(nomesColunas)

listaAfiliacao = tabela['afiliação'].tolist()

traduzirLinhas(listaAfiliacao)

tabela.head(10)

```

## Resultado
Para este desafio preferi utilizar o Jupyter Notebook para visulizar melhor os dados e inclui na tradução a coluna de afiliação para que a tabela ficasse mais legível.
O resultado final foi esta Tabela abaixo:
![Captura de tela de 2024-08-14 16-33-19](https://github.com/user-attachments/assets/086fc1d5-a3ee-4e26-a781-c76d48e2cefb)


Todos os passos podem ser visualizados no arquivo do Jupyter Notebook em anexo

# Entendendo as Bibliotecas Utilizadas:

* requests: Essa biblioteca é fundamental para fazer requisições HTTP. Ela permite enviar diferentes tipos de solicitações (GET, POST, PUT, DELETE) e lidar com as respostas das APIs.
* pandas: Ideal para manipular e analisar dados estruturados. Com o pandas, você pode converter os dados da API em DataFrames, facilitando a limpeza, transformação e análise.
* googletrans: Essa biblioteca é utilizada para traduzir textos de um idioma para outro. Ela oferece uma interface simples para realizar traduções utilizando a API do Google Translate.
