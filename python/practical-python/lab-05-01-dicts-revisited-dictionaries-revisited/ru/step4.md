# Члены класса

В отдельном словаре хранятся также методы.

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

Словарь находится в `Stock.__dict__`.

```python
{
    'cost': <function>,
   'sell': <function>,
    '__init__': <function>
}
```
