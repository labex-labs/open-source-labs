# Exercício 2.26: A Visão Geral (The Big Picture)

Usando as técnicas neste exercício, você pode escrever instruções que convertem facilmente campos de praticamente qualquer arquivo de dados orientado a colunas em um dicionário Python.

Só para ilustrar, suponha que você leia dados de um arquivo de dados diferente como este:

```python
>>> f = open('dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

Vamos converter os campos usando um truque semelhante:

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
```

Bônus: Como você modificaria este exemplo para, adicionalmente, analisar a entrada `date` em uma tupla como `(6, 11, 2007)`?

Dedique algum tempo para refletir sobre o que você fez neste exercício. Revisitaremos essas ideias um pouco mais tarde.
