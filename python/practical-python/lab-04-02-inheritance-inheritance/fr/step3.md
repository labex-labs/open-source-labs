# Exemple

Supposons que cette soit votre classe initiale :

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

Vous pouvez modifier n'importe quelle partie de cela via l'héritage.
