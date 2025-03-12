# Creating the StructureMeta Metaclass

Now that we have a way to collect all validator types, let's create a metaclass that will make these types available when defining a `Structure` subclass without requiring explicit imports.

A metaclass in Python is a class whose instances are themselves classes. The metaclass can control various aspects of class creation, including the namespace where class attributes are defined.

In our case, we'll create a metaclass that injects the validator types into the namespace of any class defined with that metaclass.

Open the `structure.py` file again and add the following code:

```bash
code structure.py
```

Add the following code at the top of the file, before the `Structure` class definition:

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

Now, modify the `Structure` class to use this metaclass:

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

Let's understand what this code does:

1. `__prepare__()` is a special method that is called before class creation to prepare the namespace where attributes will be defined. We use `ChainMap` to create a layered dictionary that includes our validator types.

2. `__new__()` is called to create the new class. We extract only the local namespace (the first dict in the `ChainMap`) to create the class, discarding the validator dictionary.

With this setup, any class that inherits from `Structure` will have access to all validator types without needing to import them explicitly.

Now let's test our implementation by creating a `Stock` class using our enhanced `Structure` base class:

```bash
cat > stock.py << EOF
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
EOF
```

If our metaclass is working correctly, we should be able to define the `Stock` class without importing the validator types.
