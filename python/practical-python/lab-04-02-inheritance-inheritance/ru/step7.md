# `__init__` и наследование

Если `__init__` переопределяется, необходимо инициализировать родителя.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Проверьте вызов `super` и `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

Вы должны вызвать метод `__init__()` на `super`, который представляет собой способ вызова предыдущей версии, как показано ранее.
