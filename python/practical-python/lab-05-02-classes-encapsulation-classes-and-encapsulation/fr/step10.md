# Attribut `__slots__`

Vous pouvez restreindre l'ensemble des noms d'attributs.

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
     ...
```

Il générera une erreur pour les autres attributs.

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in?
AttributeError: 'Stock' object has no attribute 'prices'
```

Bien que cela empêche les erreurs et restreigne l'utilisation des objets, il est en fait utilisé pour les performances et permet à Python d'utiliser la mémoire de manière plus efficace.
