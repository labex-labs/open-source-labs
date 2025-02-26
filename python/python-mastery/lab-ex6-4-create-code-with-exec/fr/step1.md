# Expérimenter avec `exec()`

Définissez un fragment de code Python dans une chaîne de caractères et essayez de l'exécuter :

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
>>>
```

Cela est intéressant, mais exécuter des fragments de code aléatoires n'est pas particulièrement utile. Un usage plus intéressant de `exec()` est de créer du code tel que des fonctions, des méthodes ou des classes. Essayez cet exemple dans lequel nous créons une fonction `__init__()` pour une classe.

```python
>>> class Stock:
        _fields = ('name','shares', 'price')

>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
        code += f'    self.{name} = {name}\n'
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Maintenant essayez la classe
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>>
```

Dans cet exemple, une fonction `__init__()` est créée directement à partir de la variable `_fields`. Il n'y a pas de trucs étranges impliquant une méthode spéciale `_init()` ou des cadres de pile.
