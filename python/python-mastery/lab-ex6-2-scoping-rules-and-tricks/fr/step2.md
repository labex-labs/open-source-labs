# Montrez-moi vos variables locales

Tout d'abord, essayez une expérience en définissant la classe suivante :

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            print(locals())

>>>
```

Maintenant, essayez d'exécuter ceci :

```python
>>> s = Stock('GOOG', 100, 490.1)
{'self': <__main__.Stock object at 0x100699b00>, 'price': 490.1, 'name': 'GOOG','shares': 100}
>>>
```

Remarquez comment le dictionnaire `locals` contient tous les arguments passés à `__init__()`. C'est intéressant. Maintenant, définissez les fonctions et les définitions de classe suivantes :

```python
>>> def _init(locs):
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

>>> class Stock:
        def __init__(self, name, shares, price):
            _init(locals())
```

Dans ce code, la fonction `_init()` est utilisée pour initialiser automatiquement un objet à partir d'un dictionnaire de variables locales passées. Vous constaterez que `help(Stock)` et les arguments de mot clé fonctionnent parfaitement.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>>
```
