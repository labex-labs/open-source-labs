# Class Members

A separate dictionary also holds the methods.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

The dictionary is in `Stock.__dict__`.

```python
{
    'cost': <function>,
    'sell': <function>,
    '__init__': <function>
}
```
