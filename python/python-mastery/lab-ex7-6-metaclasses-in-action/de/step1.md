# Die letzte Grenze

In Übung 7.3 haben wir es ermöglicht, typengeprüfte Strukturen wie folgt zu definieren:

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

Unter der Haube passiert vieles. Ein Ärger betrifft jedoch all diese Typnamen-Imports am Anfang (z.B. `String`, `PositiveInteger` usw.). Das ist genau die Art von Dingen, die zu einem `from validate import *`-Statement führen könnten. Ein interessantes Merkmal einer Metaklasse ist, dass sie dazu verwendet werden kann, den Prozess zu steuern, durch den eine Klasse definiert wird. Dies umfasst das Verwalten der Umgebung der Klasse selbst. Lassen Sie uns diese Imports angehen.

Der erste Schritt bei der Verwaltung aller Validator-Namen besteht darin, sie zu sammeln. Öffnen Sie die Datei `validate.py` und modifizieren Sie die `Validator`-Basis-Klasse mit diesem zusätzlichen Code, der wiederum `__init_subclass__()` verwendet:

```python
# validate.py

class Validator:
  ...

    # Sammeln Sie alle abgeleiteten Klassen in einem Dictionary
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
```

Das ist nicht viel, aber es erstellt einen kleinen Namensraum aller `Validator`-Unterklassen. Schauen Sie sich ihn an:

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

Jetzt, nachdem Sie das getan haben, injizieren wir diesen Namensraum in den Namensraum der aus `Structure` definierten Klassen. Definieren Sie die folgende Metaklasse:

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

In diesem Code macht die `__prepare__()`-Methode eine spezielle `ChainMap`-Zuordnung, die aus einem leeren Dictionary und einem Dictionary aller definierten Validatoren besteht. Das leere Dictionary, das zuerst aufgelistet ist, wird alle in der Klassenkörper definierten Definitionen sammeln. Das `Validator.validators`-Dictionary wird alle Typdefinitionen verfügbar machen, um als Deskriptoren oder Argumenttyp-Annotationen verwendet zu werden.

Die `__new__()`-Methode verwirft das zusätzliche Validator-Dictionary und übergibt die verbleibenden Definitionen an den Typkonstruktor. Es ist genial, aber es ermöglicht Ihnen, die lästigen Imports zu vermeiden:

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
