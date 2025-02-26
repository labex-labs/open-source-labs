# Mise en œuvre globale

En prenant les idées des deux premières parties, supprimez la méthode `__init__()` qui était initialement partie de la classe `Structure`. Ensuite, ajoutez une méthode `_init()` comme ceci :

```python
# structure.py
import sys

class Structure:
  ...
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
  ...
```

Note : La raison pour laquelle cela est défini comme une `@staticmethod` est que l'argument `self` est obtenu à partir des variables locales - il n'est pas nécessaire d'avoir en plus cet argument passé à la méthode elle-même (admittedly, c'est un peu subtil).

Maintenant, modifiez votre classe `Stock` de sorte qu'elle ressemble à ceci :

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares
```

Vérifiez que la classe fonctionne correctement, prend en charge les arguments de mot clé et a une signature d'aide correcte.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>> help(Stock)
... regardez la sortie...
>>>
```

Exécutez à nouveau vos tests unitaires dans `teststock.py`. Vous devriez voir au moins un test supplémentaire réussir. Bravo!

À ce stade, il semble que nous ayons fait un grand pas en arrière. Non seulement les classes ont besoin de la méthode `__init__()`, mais elles ont également besoin de la variable `_fields` pour que certaines autres méthodes fonctionnent (`__repr__()` et `__setattr__()`). De plus, l'utilisation de `self._init()` semble assez truquée. Nous allons travailler sur ceci, mais soyez patient.
