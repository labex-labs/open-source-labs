# `__init__` und Vererbung

Wenn `__init__` neu definiert wird, ist es unerlässlich, die Elternklasse zu initialisieren.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Überprüfe den Aufruf von `super` und `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

Du solltest die `__init__()`-Methode auf dem `super` aufrufen, was der Weg ist, um die vorherige Version aufzurufen, wie zuvor gezeigt.
