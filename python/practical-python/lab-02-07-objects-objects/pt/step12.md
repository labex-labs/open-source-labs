# Exercício 2.25: Criando dicionários

Lembre-se de como a função `dict()` pode facilmente criar um dicionário se você tiver uma sequência de nomes de chaves e valores? Vamos criar um dicionário a partir dos cabeçalhos das colunas:

```python
>>> headers
['name', 'shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```

Claro, se você domina as list-comprehensions, pode fazer toda a conversão em uma única etapa usando uma dict-comprehension:

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```
