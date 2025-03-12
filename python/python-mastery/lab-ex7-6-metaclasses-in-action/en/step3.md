# Creating the StructureMeta Metaclass

Now, let's talk about what we're going to do next. We've found a way to collect all validator types. Our next step is to create a metaclass. But what exactly is a metaclass? In Python, a metaclass is a special kind of class. Its instances are classes themselves. This means that a metaclass can control how a class is created. It can manage the namespace where class attributes are defined.

In our situation, we want to create a metaclass that will make the validator types available when we define a `Structure` subclass. We don't want to have to import these validator types explicitly every time.

Let's start by opening the `structure.py` file again. You can use the following command to open it:

```bash
code structure.py
```

Once the file is open, we need to add some code at the top, before the `Structure` class definition. This code will define our metaclass.

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

Now that we've defined the metaclass, we need to modify the `Structure` class to use it. This way, any class that inherits from `Structure` will benefit from the metaclass's functionality.

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

Let's break down what this code does:

1. The `__prepare__()` method is a special method in Python. It's called before the class is created. Its job is to prepare the namespace where the class attributes will be defined. We use `ChainMap` here. `ChainMap` is a useful tool that creates a layered dictionary. In our case, it includes our validator types, making them accessible in the class namespace.

2. The `__new__()` method is responsible for creating the new class. We extract only the local namespace, which is the first dictionary in the `ChainMap`. We discard the validator dictionary because we've already made the validator types available in the namespace.

With this setup, any class that inherits from `Structure` will have access to all validator types without the need to import them explicitly.

Now, let's test our implementation. We'll create a `Stock` class using our enhanced `Structure` base class.

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

If our metaclass is working correctly, we should be able to define the `Stock` class without importing the validator types. This is because the metaclass has already made them available in the namespace.
