# Пример

Предположим, что это ваш исходный класс:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Вы можете изменить любую часть этого с использованием наследования.
