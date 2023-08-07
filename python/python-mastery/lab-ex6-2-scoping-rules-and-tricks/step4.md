# Putting it Together

Taking the ideas in the first two parts, delete the `__init__()` method that was originally part of the `Structure` class. Next, add an `_init()` method like this:

```python
# structure.py
import sys

class Structure:
    ...
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
    ...
```

Note: The reason this is defined as a `@staticmethod` is that the `self` argument is obtained from the locals--there's no need to additionally have it passed as an argument to the method itself (admittedly this is a bit subtle).

Now, modify your `Stock` class so that it looks like the following:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name','shares','price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares
```

Verify that the class works properly, supports keyword arguments, and has a proper help signature.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>> help(Stock)
... look at the output ...
>>>
```

Run your unit tests in `teststock.py` again. You should see at least one more test pass. Yay!

At this point, it's going to look like we just took a giant step backwards. Not only do the classes need the `__init__()` method, they also need the `_fields` variable for some of the other methods to work (`__repr__()` and `__setattr__()`). Plus, the use of `self._init()` looks pretty hacky. We'll work on this, but be patient.
