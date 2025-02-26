# Utilisation de la fonction zip()

La fonction `zip()` est le plus souvent utilisée pour associer des données. Par exemple, rappelez-vous que vous avez créé une variable `headers` :

```python
>>> headers
['name','shares', 'price']
>>>
```

Cela peut être utile pour combiner avec les autres données de ligne :

```python
>>> row = rows[0]
>>> row
['AA', '100', '32.20']
>>> for col, val in zip(headers, row):
        print(col, val)

name AA
shares 100
price 32.20
>>>
```

Ou peut-être que vous pouvez l'utiliser pour créer un dictionnaire :

```python
>>> dict(zip(headers, row))
{'name': 'AA','shares': '100', 'price': '32.20'}
>>>
```

Ou peut-être une séquence de dictionnaires :

```python
>>> for row in rows:
        record = dict(zip(headers, row))
        print(record)

{'name': 'AA','shares': '100', 'price': '32.20'}
{'name': 'IBM','shares': '50', 'price': '91.10'}
{'name': 'CAT','shares': '150', 'price': '83.44'}
{'name': 'MSFT','shares': '200', 'price': '51.23'}
{'name': 'GE','shares': '95', 'price': '40.37'}
{'name': 'MSFT','shares': '50', 'price': '65.10'}
{'name': 'IBM','shares': '100', 'price': '70.44'}
>>>
```
