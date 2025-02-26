# Constructeurs alternatifs

Peut-être la création d'un `Stock` à partir d'une ligne de données brutes est-elle mieux gérée par un constructeur alternatif. Modifiez la classe `Stock` de sorte qu'elle ait une variable de classe `types` et une méthode de classe `from_row()` comme ceci :

```python
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
  ...
```

Voici comment le tester :

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock.from_row(row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>> s.cost()
3220.0000000000005
>>>
```

Observez attentivement comment les valeurs de chaîne de caractères dans la ligne ont été converties en un type approprié.
