# `__init__` y herencia

Si se redefine `__init__`, es esencial inicializar al padre.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Comprueba la llamada a `super` y `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

Debes llamar al método `__init__()` en el `super` que es la forma de llamar a la versión anterior como se mostró anteriormente.
