# Sobrescrita (Overriding)

Às vezes, uma classe estende um método existente, mas deseja usar a implementação original dentro da redefinição. Para isso, use `super()`:

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

Use `super()` para chamar a versão anterior.

_Atenção: No Python 2, a sintaxe era mais verbosa._

```python
actual_cost = super(MyStock, self).cost()
```
