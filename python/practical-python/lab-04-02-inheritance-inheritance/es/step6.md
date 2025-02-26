# Sobreescritura

A veces una clase extiende un método existente, pero desea utilizar la implementación original dentro de la redefinición. Para esto, use `super()`:

```python
class Stock:
  ...
    def cost(self):
        return self.shares * self.price
  ...

class MyStock(Stock):
    def cost(self):
        # Comprueba la llamada a `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

Use `super()` para llamar a la versión anterior.

_Advertencia: En Python 2, la sintaxis era más detallada._

```python
actual_cost = super(MyStock, self).cost()
```
