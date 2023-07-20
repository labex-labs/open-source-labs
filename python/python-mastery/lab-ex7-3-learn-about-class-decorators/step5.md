# Method Argument Checking

Remember that `@validated` decorator you wrote in the last part?
Let's modify the `@validate_attributes` decorator so that any method
in the class with annotations gets wrapped by `@validated`
automatically. This allows you to put enforced annotations on methods
such as the `sell()` method:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

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

You'll find that `sell()` now enforces the argument.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.sell(-25)
Traceback (most recent call last):
  ...
TypeError: Bad Arguments
  nshares: must be >= 0
>>>
```

Yes, this starting to get very interesting now. The combination of a class decorator and
inheritance is a powerful force.
