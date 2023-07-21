# Overriding

Sometimes a class extends an existing method, but it wants to use the
original implementation inside the redefinition. For this, use `super()`:

```python
class Stock:
    ...
    def cost(self):
        return self.shares * self.price
    ...

class MyStock(Stock):
    def cost(self):
        # Check the call to `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

Use `super()` to call the previous version.

_Caution: In Python 2, the syntax was more verbose._

```python
actual_cost = super(MyStock, self).cost()
```
