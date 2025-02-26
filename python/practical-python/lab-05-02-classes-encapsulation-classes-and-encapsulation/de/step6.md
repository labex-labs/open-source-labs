# Verwaltete Attribute

Eine Möglichkeit: Einführung von Zugangsmethoden.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Funktion, die die "get"-Operation abdeckt
    def get_shares(self):
        return self._shares

    # Funktion, die die "set"-Operation abdeckt
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Erwartet einen int')
        self._shares = value
```

Schade, dass damit all unseren bestehenden Code kaputt geht. `s.shares = 50` wird zu `s.set_shares(50)`
