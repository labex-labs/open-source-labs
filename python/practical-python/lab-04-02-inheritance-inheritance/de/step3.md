# Beispiel

Angenommen, das ist deine Ausgangsklasse:

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

Du kannst jeder Teil davon über Vererbung ändern.
