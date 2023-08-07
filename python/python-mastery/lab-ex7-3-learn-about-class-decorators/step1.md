# Descriptors Revisited

In [Exercise 4.3](ex4_3.md) you defined some descriptors that
allowed a user to define classes with type-checked attributes like
this:

```python
from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
    ...
```

Modify your `Stock` class so that it includes the above descriptors
and now looks like this (see [Exercise 6.4](ex6_4.md)):

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```

Run the unit tests in `teststock.py`. You should see a significant
number of tests passing with the addition of type checking.
Excellent.
