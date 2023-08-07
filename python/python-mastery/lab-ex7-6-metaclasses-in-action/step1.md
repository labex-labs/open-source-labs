# The Final Frontier

In [Exercise 7.3](ex7_3.md), we made it possible to define type-checked structures as follows:

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

There are a lot of things going on under the covers. However, one annoyance concerns all of those type-name imports at the top (e.g., `String`, `PositiveInteger`, etc.). That's just the kind of thing that might lead to a `from validate import *` statement. One interesting thing about a metaclass is that it can be used to control the process by which a class gets defined. This includes managing the environment of a class definition itself. Let's tackle those imports.

The first step in managing all of the validator names is to collect them. Go to the file `validate.py` and modify the `Validator` base class with this extra bit of code involving `__init_subclass__()` again:

```python
# validate.py

class Validator:
    ...

    # Collect all derived classes into a dict
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
```

That's not much, but it's creating a little namespace of all of the `Validator` subclasses. Take a look at it:

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

Now that you've done that, let's inject this namespace into namespace of classes defined from `Structure`. Define the following metaclass:

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

In this code, the `__prepare__()` method is making a special `ChainMap` mapping that consists of an empty dictionary and a dictionary of all of the defined validators. The empty dictionary that's listed first is going to collect all of the definitions made inside the class body. The `Validator.validators` dictionary is going to make all of the type definitions available to for use as descriptors or argument type annotations.

The `__new__()` method discards extra the validator dictionary and passes the remaining definitions onto the type constructor. It's ingenious, but it lets you drop the annoying imports:

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
