# Attributs gérés

Une approche : introduire des méthodes d'accès.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Fonction qui couche l'opération "get"
    def get_shares(self):
        return self._shares

    # Fonction qui couche l'opération "set"
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
```

Dommage que cela brise tout notre code existant. `s.shares = 50` devient `s.set_shares(50)`
