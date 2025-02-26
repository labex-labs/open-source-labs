# La Frontière Finale

Dans l'exercice 7.3, nous avons rendu possible la définition de structures vérifiées par type comme suit :

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Il y a beaucoup de choses qui se passent sous le capot. Cependant, un inconvénient concerne toutes ces importations de noms de type en haut (par exemple, `String`, `PositiveInteger`, etc.). C'est exactement le genre de chose qui pourrait conduire à une instruction `from validate import *`. Une chose intéressante à propos d'une métaclasse est qu'elle peut être utilisée pour contrôler le processus par lequel une classe est définie. Cela inclut la gestion de l'environnement de la définition de la classe elle-même. Allons-y pour gérer ces importations.

La première étape pour gérer tous les noms de validateurs est de les collecter. Allez dans le fichier `validate.py` et modifiez la classe de base `Validator` avec ce bout supplémentaire de code impliquant `__init_subclass__()` encore une fois :

```python
# validate.py

class Validator:
  ...

    # Collecte toutes les classes dérivées dans un dictionnaire
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
```

Ce n'est pas beaucoup, mais cela crée un petit espace de noms de toutes les sous-classes de `Validator`. Jetez-y un coup d'œil :

```python
>>> from validate import Validator
>>> Validator.validators
{'Float': <class 'validate.Float'>,
 'Integer': <class 'validate.Integer'>,
 'NonEmpty': <class 'validate.NonEmpty'>,
 'NonEmptyString': <class 'validate.NonEmptyString'>,
 'Positive': <class 'validate.Positive'>,
 'PositiveFloat': <class 'validate.PositiveFloat'>,
 'PositiveInteger': <class 'validate.PositiveInteger'>,
 'String': <class 'validate.String'>,
 'Typed': <class 'validate.Typed'>}
>>>
```

Maintenant que vous avez fait cela, injectons cet espace de noms dans l'espace de noms des classes définies à partir de `Structure`. Définissez la métaclasse suivante :

```python
# structure.py
...

from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
  ...
```

Dans ce code, la méthode `__prepare__()` crée une spéciale carte de mappage `ChainMap` qui est composée d'un dictionnaire vide et d'un dictionnaire de tous les validateurs définis. Le dictionnaire vide qui est listé en premier va collecter toutes les définitions faites dans le corps de la classe. Le dictionnaire `Validator.validators` va rendre toutes les définitions de type disponibles pour être utilisées comme descripteurs ou annotations de type d'arguments.

La méthode `__new__()` jette le dictionnaire de validateur supplémentaire et passe les définitions restantes au constructeur de type. C'est ingénieux, mais cela vous permet d'éliminer les importations gênantes :

```python
# stock.py

from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```
