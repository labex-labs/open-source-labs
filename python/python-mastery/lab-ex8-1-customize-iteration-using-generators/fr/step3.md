# Le pouvoir surprenant de l'itération

Python utilise l'itération de manières que vous ne pouvez pas vous attendre. Une fois que vous avez ajouté `__iter__()` à la classe `Structure`, vous allez constater qu'il est facile de faire toutes sortes de nouvelles opérations. Par exemple, les conversions en séquences et le déballage :

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> list(s)
['GOOG', 100, 490.1]
>>> tuple(s)
('GOOG', 100, 490.1)
>>> name, shares, price = s
>>> name
'GOOG'
>>> shares
100
>>> price
490.1
>>>
```

Pendant que nous y sommes, nous pouvons maintenant ajouter un opérateur de comparaison à notre classe `Structure` :

```python
# structure.py
class Structure(metaclass=StructureMeta):
 ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
 ...
```

Vous devriez maintenant être en mesure de comparer des objets :

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
True
>>>
```

Essayez de lancer à nouveau vos tests unitaires `teststock.py`. Tout devrait passer maintenant. Excellent.
