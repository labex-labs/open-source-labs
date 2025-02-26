# Itération et déballage de base

L'instruction `for` itère sur n'importe quelle séquence de données. Par exemple :

```python
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>>
```

Déballez les valeurs dans des variables distinctes si nécessaire :

```python
>>> for name, shares, price in rows:
        print(name, shares, price)

AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
>>>
```

Il est assez courant d'utiliser `_` ou `__` comme variable jetable si vous n'avez pas besoin d'une ou plusieurs des valeurs. Par exemple :

```python
>>> for name, _, price in rows:
        print(name, price)

AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
>>>
```

Si vous ne savez pas combien de valeurs sont déballées, vous pouvez utiliser `*` comme joker. Essayez cet exemple pour regrouper les données par nom :

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for name, *data in rows:
        byname[name].append(data)

>>> byname['IBM']
[['50', '91.10'], ['100', '70.44']]
>>> byname['CAT']
[['150', '83.44']]
>>> for shares, price in byname['IBM']:
        print(shares, price)

50 91.10
100 70.44
>>>
```
