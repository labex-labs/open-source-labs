# Opérateurs mathématiques

Vous pouvez faire en sorte qu'un objet fonctionne avec divers opérateurs mathématiques si vous implémentez les méthodes appropriées pour lui. Cependant, il vous incombe de reconnaître les autres types de données et d'implémenter le code de conversion approprié. Modifiez la classe `MutInt` en lui donnant une méthode `__add__()` comme suit :

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
```

Avec ce changement, vous devriez constater que vous pouvez additionner à la fois des entiers et des entiers mutables. Le résultat est une instance de `MutInt`. Ajouter d'autres types de nombres entraîne une erreur :

```python
>>> a = MutInt(3)
>>> b = a + 10
>>> b
MutInt(13)
>>> b.value = 23
>>> c = a + b
>>> c
MutInt(26)
>>> a + 3.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'float'
>>>
```

Un problème avec le code est qu'il ne fonctionne pas lorsque l'ordre des opérandes est inversé. Considérez :

```python
>>> a + 10
MutInt(13)
>>> 10 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'MutInt'
>>>
```

Cela se produit parce que le type `int` ne connaît pas `MutInt` et il est confus. Cela peut être corrigé en ajoutant une méthode `__radd__()`. Cette méthode est appelée si la première tentative d'appel de `__add__()` n'a pas fonctionné avec l'objet fourni.

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__    # Opérandes inversées
```

Avec ce changement, vous constaterez que l'addition fonctionne :

```python
>>> a = MutInt(3)
>>> a + 10
MutInt(13)
>>> 10 + a
MutInt(13)
>>>
```

Puisque notre entier est mutable, vous pouvez également le faire reconnaître l'opérateur d'addition-incrémentation en place `+=` en implémentant la méthode `__iadd__()` :

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Cela permet des utilisations intéressantes comme celle-ci :

```python
>>> a = MutInt(3)
>>> b = a
>>> a += 10
>>> a
MutInt(13)
>>> b                 # Remarquez que b change également
MutInt(13)
>>>
```

Il peut sembler un peu étrange que `b` change également, mais il existe des fonctionnalités subtiles comme cela avec les objets Python intégrés. Par exemple :

```python
>>> a = [1,2,3]
>>> b = a
>>> a += [4,5]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]

>>> c = (1,2,3)
>>> d = c
>>> c += (4,5)
>>> c
(1, 2, 3, 4, 5)
>>> d                  # Expliquez la différence avec les listes
(1, 2, 3)
>>>
```
