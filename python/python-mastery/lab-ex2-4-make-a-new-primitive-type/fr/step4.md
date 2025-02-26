# Comparaisons

Un problème est que les comparaisons ne fonctionnent toujours pas. Par exemple :

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
False
>>> a == 3
False
>>>
```

Vous pouvez corriger cela en ajoutant une méthode `__eq__()`. D'autres méthodes telles que `__lt__()`, `__le__()`, `__gt__()`, `__ge__()` peuvent être utilisées pour implémenter d'autres comparaisons. Par exemple :

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

Essayez :

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
True
>>> c = MutInt(4)
>>> a < c
True
>>> a <= c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<=' not supported between instances of 'MutInt' and 'MutInt'
>>>
```

La raison pour laquelle l'opérateur `<=` échoue est qu'aucune méthode `__le__()` n'a été fournie. Vous pourriez la coder séparément, mais une manière plus simple de l'obtenir est d'utiliser le décorateur `@total_ordering` :

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

`@total_ordering` remplit les méthodes de comparaison manquantes pour vous, pourvu que vous fournissiez au minimum un opérateur d'égalité et l'une des autres relations.
