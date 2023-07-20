# Applying Decorators via Inheritance

Having to specify the class decorator itself is kind of annoying. Modify the
`Structure` class with the following `__init_subclass__()` method:

```python
# structure.py

class Structure:
    ...
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

Once you've made this change, you should be able to drop the decorator entirely and
solely rely on inheritance. It's inheritance plus some hidden magic!

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

    def sell(self, nshares):
        self.shares -= nshares
```

Now, the code is really starting to go places. In fact, it almost
looks normal. Let's keep pushing it.
