# Exercício 2.23: Extraindo Dados de Arquivos CSV

Saber como usar várias combinações de list, set e dictionary comprehensions (compreensões de lista, conjunto e dicionário) pode ser útil em várias formas de processamento de dados. Aqui está um exemplo que mostra como extrair colunas selecionadas de um arquivo CSV.

Primeiro, leia uma linha de informações de cabeçalho de um arquivo CSV:

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time', 'shares', 'price']
>>>
```

Em seguida, defina uma variável que lista as colunas que você realmente se importa:

```python
>>> select = ['name', 'shares', 'price']
>>>
```

Agora, localize os índices das colunas acima no arquivo CSV de origem:

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

Finalmente, leia uma linha de dados e transforme-a em um dicionário usando uma dictionary comprehension (compreensão de dicionário):

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

Se você está se sentindo confortável com o que acabou de acontecer, leia o resto do arquivo:

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'},
  {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'},
  {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

Nossa, você acabou de reduzir grande parte da função `read_portfolio()` a uma única instrução.
