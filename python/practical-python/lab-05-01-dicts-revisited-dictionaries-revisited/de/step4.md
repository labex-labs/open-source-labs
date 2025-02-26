# Klasseneigenschaften

Ein separates Wörterbuch enthält auch die Methoden.

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

Das Wörterbuch befindet sich in `Stock.__dict__`.

```python
{
    'cost': <function>,
   'sell': <function>,
    '__init__': <function>
}
```
