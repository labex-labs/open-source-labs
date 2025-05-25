# Exercício 2.21: Consultas de Dados

Experimente os seguintes exemplos de várias consultas de dados.

Primeiro, uma lista de todas as participações do portfólio com mais de 100 ações.

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}]
>>>
```

Todas as participações do portfólio para as ações MSFT e IBM.

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 51.23, 'name': 'MSFT', 'shares': 200},
  {'price': 65.1, 'name': 'MSFT', 'shares': 50}, {'price': 70.44, 'name': 'IBM', 'shares': 100}]
>>>
```

Uma lista de todas as participações do portfólio que custam mais de \$10000.

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}]
>>>
```
