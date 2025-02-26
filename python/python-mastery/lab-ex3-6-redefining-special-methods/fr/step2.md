# Rendre les objets comparables

Que se passe-t-il si vous créez deux objets `Stock` identiques et que vous essayez de les comparer? Découvrez-le :

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
False
>>>
```

Vous pouvez corriger ce problème en donnant à la classe `Stock` une méthode `__eq__()`. Par exemple :

```python
class Stock:
  ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
  ...
```

Apportez ces modifications et essayez à nouveau de comparer deux objets.
