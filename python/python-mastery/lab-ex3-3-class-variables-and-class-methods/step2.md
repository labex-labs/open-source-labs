# Alternate constructors

Perhaps the creation of a `Stock` from a row of raw data is better handled by an alternate constructor. Modify the `Stock` class so that it has a `types` class variable and `from_row()` class method like this:

```python
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
    ...
```

Here's how to test it:

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock.from_row(row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>> s.cost()
3220.0000000000005
>>>
```

Carefully observe how the string values in the row have been converted to a proper type.
