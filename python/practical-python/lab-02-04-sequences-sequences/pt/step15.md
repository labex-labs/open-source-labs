# Exercício 2.16: Usando a função `zip()`

No arquivo `portfolio.csv`, a primeira linha contém os cabeçalhos das colunas. Em todo o código anterior, estávamos descartando-os.

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'shares', 'price']
>>>
```

No entanto, e se você pudesse usar os cabeçalhos para algo útil? É aqui que a função `zip()` entra em cena. Primeiro, tente isso para emparelhar os cabeçalhos do arquivo com uma linha de dados:

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

Observe como `zip()` emparelhou os cabeçalhos das colunas com os valores das colunas. Usamos `list()` aqui para transformar o resultado em uma lista para que você possa vê-lo. Normalmente, `zip()` cria um iterador que deve ser consumido por um loop for.

Este emparelhamento é um passo intermediário para construir um dicionário. Agora tente isto:

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

Esta transformação é um dos truques mais úteis de se saber ao processar muitos arquivos de dados. Por exemplo, suponha que você queira que o programa `pcost.py` funcione com vários arquivos de entrada, mas sem levar em consideração o número real da coluna onde o nome, as ações e o preço aparecem.

Modifique a função `portfolio_cost()` em `pcost.py` para que ela se pareça com isto:

```python
# pcost.py

def portfolio_cost(filename):
    ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        ...
```

Agora, teste sua função em um arquivo de dados completamente diferente `portfoliodate.csv` que se parece com isto:

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

Se você fez certo, descobrirá que seu programa ainda funciona, mesmo que o arquivo de dados tenha um formato de coluna completamente diferente do anterior. Isso é legal!

A mudança feita aqui é sutil, mas significativa. Em vez de `portfolio_cost()` ser codificado para ler um único formato de arquivo fixo, a nova versão lê qualquer arquivo CSV e seleciona os valores de interesse dele. Contanto que o arquivo tenha as colunas necessárias, o código funcionará.

Modifique o programa `report.py` que você escreveu na Seção 2.3 para que ele use a mesma técnica para selecionar os cabeçalhos das colunas.

Tente executar o programa `report.py` no arquivo `portfoliodate.csv` e veja que ele produz a mesma resposta de antes.
