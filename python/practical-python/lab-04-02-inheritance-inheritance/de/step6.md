# Überschreiben

Manchmal erweitert eine Klasse eine vorhandene Methode, aber möchte die ursprüngliche Implementierung innerhalb der Neudefinition verwenden. Dazu nutzt man `super()`:

```python
class Stock:
  ...
    def cost(self):
        return self.shares * self.price
  ...

class MyStock(Stock):
    def cost(self):
        # Überprüfe den Aufruf von `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

Verwende `super()`, um die vorherige Version aufzurufen.

_Hinweis: In Python 2 war die Syntax umständlicher._

```python
actual_cost = super(MyStock, self).cost()
```
