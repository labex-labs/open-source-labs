# `__init__` e herança (inheritance)

Se `__init__` for redefinido, é essencial inicializar o pai.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to `super` and `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

Você deve chamar o método `__init__()` no `super`, que é a maneira de chamar a versão anterior, como mostrado anteriormente.
