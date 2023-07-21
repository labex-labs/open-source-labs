# Managed Attributes

One approach: introduce accessor methods.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Function that layers the "get" operation
    def get_shares(self):
        return self._shares

    # Function that layers the "set" operation
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
```

Too bad that this breaks all of our existing code. `s.shares = 50`
becomes `s.set_shares(50)`
