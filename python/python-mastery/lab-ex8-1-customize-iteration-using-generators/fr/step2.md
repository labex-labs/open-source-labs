# Ajout d'une itération aux objets

Si vous avez créé une classe personnalisée, vous pouvez la rendre compatible avec l'itération en définissant une méthode spéciale `__iter__()`. `__iter__()` renvoie un itérateur en résultat. Comme montré dans l'exemple précédent, une manière simple de le faire est de définir `__iter__()` comme un générateur.

Dans les exercices précédents, vous avez défini une classe de base `Structure`. Ajoutez une méthode `__iter__()` à cette classe qui produit les valeurs d'attribut dans l'ordre. Par exemple :

```python
class Structure(metaclass=StructureMeta):
  ...
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
  ...
```

Une fois que vous avez fait cela, vous devriez être en mesure d'itérer sur les attributs de l'instance comme ceci :

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> for val in s:
        print(val)
GOOG
100
490.1
>>>
```
