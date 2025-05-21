# Trabalhando com Dicionários e Dados CSV

Vamos começar examinando um conjunto de dados simples sobre participações acionárias. Nesta etapa, você aprenderá como ler dados de um arquivo CSV e armazená-los em um formato estruturado usando dicionários.

Um arquivo CSV (Valores Separados por Vírgula) é uma maneira comum de armazenar dados tabulares, onde cada linha representa uma linha e os valores são separados por vírgulas. Dicionários em Python são uma estrutura de dados poderosa que permite armazenar pares chave-valor. Ao usar dicionários, podemos organizar os dados do arquivo CSV de uma maneira mais significativa.

Primeiro, crie um novo arquivo Python no WebIDE seguindo estas etapas:

1. Clique no botão "New File" (Novo Arquivo) no WebIDE
2. Nomeie o arquivo `readport.py`
3. Copie e cole o seguinte código no arquivo:

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Este código define uma função `read_portfolio` que realiza várias tarefas importantes:

1. Ele abre um arquivo CSV especificado pelo parâmetro `filename`. A função `open` é usada para acessar o arquivo, e a instrução `with` garante que o arquivo seja fechado corretamente depois de terminarmos de lê-lo.
2. Ele pula a linha do cabeçalho. A linha do cabeçalho geralmente contém os nomes das colunas no arquivo CSV. Usamos `next(rows)` para mover o iterador para a próxima linha, efetivamente pulando o cabeçalho.
3. Para cada linha de dados, ele cria um dicionário. As chaves do dicionário são 'name', 'shares' e 'price'. Essas chaves nos ajudarão a acessar os dados de uma maneira mais intuitiva.
4. Ele converte as ações em inteiros e os preços em números de ponto flutuante. Isso é importante porque os dados lidos do arquivo CSV estão inicialmente em formato de string, e precisamos de valores numéricos para cálculos.
5. Ele adiciona cada dicionário a uma lista chamada `portfolio`. Esta lista conterá todos os registros do arquivo CSV.
6. Finalmente, ele retorna a lista completa de dicionários.

Agora, vamos criar um arquivo para os dados de trânsito. Crie um novo arquivo chamado `readrides.py` com este conteúdo:

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

Esta função `read_rides_as_dicts` funciona de maneira semelhante à função `read_portfolio`. Ela lê um arquivo CSV relacionado aos dados de ônibus da CTA, pula a linha do cabeçalho, cria um dicionário para cada linha de dados e armazena esses dicionários em uma lista.

Agora, vamos testar a função `read_portfolio` abrindo um terminal no WebIDE:

1. Clique no menu "Terminal" e selecione "New Terminal" (Novo Terminal)
2. Inicie o interpretador Python digitando `python3`
3. Execute os seguintes comandos:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

A função `pprint` (pretty print - impressão formatada) é usada aqui para exibir os dados em um formato mais legível. Cada item na lista é um dicionário que representa uma participação acionária. O dicionário tem as seguintes chaves:

- Um símbolo da ação (`name`): Esta é a abreviação usada para identificar a ação.
- Número de ações possuídas (`shares`): Isso indica quantas ações da ação são mantidas.
- Preço de compra por ação (`price`): Este é o preço pelo qual cada ação foi comprada.

Observe que algumas ações como 'MSFT' e 'IBM' aparecem várias vezes. Elas representam diferentes compras da mesma ação, que podem ter sido feitas em momentos e preços diferentes.
