# `__init__` 与继承

如果重新定义了 `__init__`，那么初始化父类是至关重要的。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # 检查对 `super` 和 `__init__` 的调用
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

你应该在 `super` 上调用 `__init__()` 方法，这是如前所示调用上一个版本的方式。
