# Conversions

Votre nouveau type primitif est presque terminé. Vous voudriez peut-être lui donner la capacité de travailler avec certaines conversions courantes. Par exemple :

```python
>>> a = MutInt(3)
>>> int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>> float(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>>
```

Vous pouvez donner à votre classe des méthodes `__int__()` et `__float__()` pour corriger cela :

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

...

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
```

Maintenant, vous pouvez convertir correctement :

```python
>>> a = MutInt(3)
>>> int(a)
3
>>> float(a)
3.0
>>>
```

En règle générale, Python ne convertit jamais automatiquement les données cependant. Ainsi, même si vous avez donné à la classe une méthode `__int__()`, `MutInt` ne fonctionnera toujours pas dans toutes les situations où un entier pourrait être attendu. Par exemple, l'indexation :

```python
>>> names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
>>> a = MutInt(1)
>>> names[a]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not MutInt
>>>
```

Cela peut être corrigé en donnant à `MutInt` une méthode `__index__()` qui produit un entier. Modifiez la classe comme ceci :

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

...

    def __int__(self):
        return self.value

    __index__ = __int__     # Faire fonctionner l'indexation
```

**Discussion**

Créer un nouveau type de données primitif est en fait l'une des tâches de programmation les plus complexes en Python. Il y a beaucoup de cas limites et de problèmes de bas niveau à prendre en compte - en particulier en ce qui concerne la manière dont votre type interagit avec les autres types Python. Probablement la chose clé à garder à l'esprit est que vous pouvez personnaliser presque tous les aspects de la manière dont un objet interagit avec le reste de Python si vous connaissez les protocoles de base. Si vous allez faire cela, il est recommandé de regarder le code existant pour quelque chose de similaire à ce que vous essayez de créer.
