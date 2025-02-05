# 重写

有时一个类扩展了一个现有方法，但它希望在重新定义时使用原始实现。为此，请使用 `super()`：

```python
class Stock:
  ...
    def cost(self):
        return self.shares * self.price
  ...

class MyStock(Stock):
    def cost(self):
        # 检查对 `super` 的调用
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

使用 `super()` 来调用上一个版本。

_注意：在 Python 2 中，语法更冗长。_

```python
actual_cost = super(MyStock, self).cost()
```
