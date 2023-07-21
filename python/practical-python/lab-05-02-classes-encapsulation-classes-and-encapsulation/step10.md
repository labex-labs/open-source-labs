# `__slots__` Attribute

You can restrict the set of attributes names.

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
        ...
```

It will raise an error for other attributes.

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AttributeError: 'Stock' object has no attribute 'prices'
```

Although this prevents errors and restricts usage of objects, it's actually used for performance and
makes Python use memory more efficiently.
