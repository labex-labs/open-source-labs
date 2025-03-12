# Implementing the Advanced Initialization in Structure

Now that we've explored two powerful techniques for accessing function arguments, let's update our `Structure` class to use them. Open the `structure.py` file in the code editor:

```bash
cd ~/project
code structure.py
```

Replace the content of the file with the following code:

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

Notice that we've:

1. Removed the old `__init__()` method since subclasses will define their own
2. Added a new `_init()` static method that uses frame inspection
3. Kept the `__repr__()` method for nice string representation
4. Added a `__setattr__()` method to enforce attribute validation

Now, let's update the `Stock` class. Open the `stock.py` file:

```bash
code stock.py
```

Replace its content with:

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

The key change here is that our `__init__` method now calls `self._init()` instead of manually setting each attribute. The `_init()` method uses frame inspection to automatically capture and set all parameters as attributes.

Let's test our implementation by running the unit tests:

```bash
cd ~/project
python3 teststock.py
```

You should see that all tests pass, including the test for keyword arguments that failed before.

Let's also check the help documentation for our `Stock` class:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Now you should see a proper signature for the `__init__` method, showing all the parameter names.

Finally, let's interactively test that keyword arguments work as expected:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

You should see the Stock object properly created with the specified attributes.

With this implementation, we've achieved a much more flexible and user-friendly class initialization system that:

1. Preserves proper function signatures in documentation
2. Supports both positional and keyword arguments
3. Requires minimal boilerplate code in subclasses
