# Challenge: Eliminating names

Modify the `typedproperty.py` code so that attribute names are no-longer required:

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Hint: To do this, recall the `__set_name__()` method of descriptor objects that gets called when descriptors are placed in a class definition.
