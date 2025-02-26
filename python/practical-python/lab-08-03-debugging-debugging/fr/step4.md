# Débogage avec l'instruction print

Le débogage avec l'instruction `print()` est assez courant.

_Conseil : assurez-vous d'utiliser `repr()`_

```python
def spam(x):
    print('DEBUG:', repr(x))
  ...
```

`repr()` vous montre une représentation exacte d'une valeur. Pas la sortie d'affichage _élégante_.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# SANS `repr`
>>> print(x)
3.4
# AVEC `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
