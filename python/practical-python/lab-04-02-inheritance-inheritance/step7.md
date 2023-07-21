# `__init__` and inheritance

If `__init__` is redefined, it is essential to initialize the parent.

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

You should call the `__init__()` method on the `super` which is the
way to call the previous version as shown previously.
