# Exercício 2.2: Dicionários como uma estrutura de dados (data structure)

Uma alternativa a uma tupla é criar um dicionário em vez disso.

```python
>>> d = {
        'name' : row[0],
        'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA', 'shares': 100, 'price': 32.2 }
>>>
```

Calcule o custo total desta participação:

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

Compare este exemplo com o mesmo cálculo envolvendo tuplas acima. Mude o número de ações para 75.

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA', 'shares': 75, 'price': 32.2 }
>>>
```

Ao contrário das tuplas, os dicionários podem ser livremente modificados. Adicione alguns atributos:

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```
