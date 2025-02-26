# La última frontera

En el Ejercicio 7.3, hicimos posible definir estructuras con comprobación de tipos de la siguiente manera:

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

Hay muchas cosas que suceden por debajo de los paneles. Sin embargo, una molestia concierne a todas esas importaciones de nombres de tipo en la parte superior (por ejemplo, `String`, `PositiveInteger`, etc.). Eso es justo el tipo de cosa que podría llevar a una declaración `from validate import *`. Una cosa interesante sobre una metaclase es que se puede utilizar para controlar el proceso por el cual se define una clase. Esto incluye administrar el entorno de la definición de una clase en sí misma. Vamos a abordar esas importaciones.

El primer paso para administrar todos los nombres de validadores es recopilarlos. Vaya al archivo `validate.py` y modifique la clase base `Validator` con este trozo adicional de código que involucra `__init_subclass__()` nuevamente:

```python
# validate.py

class Validator:
 ...

    # Recopile todas las clases derivadas en un diccionario
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
```

Eso no es mucho, pero está creando un pequeño espacio de nombres de todas las subclases de `Validator`. Echa un vistazo:

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

Ahora que has hecho eso, vamos a inyectar este espacio de nombres en el espacio de nombres de las clases definidas a partir de `Structure`. Defina la siguiente metaclase:

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

En este código, el método `__prepare__()` está creando un `ChainMap` especial que consta de un diccionario vacío y un diccionario de todos los validadores definidos. El diccionario vacío que se lista primero va a recopilar todas las definiciones hechas dentro del cuerpo de la clase. El diccionario `Validator.validators` va a hacer que todas las definiciones de tipo estén disponibles para su uso como descriptores o anotaciones de tipo de argumento.

El método `__new__()` descarta el diccionario de validadores adicional y pasa las definiciones restantes al constructor de tipo. Es ingenioso, pero te permite eliminar las importaciones molestas:

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
