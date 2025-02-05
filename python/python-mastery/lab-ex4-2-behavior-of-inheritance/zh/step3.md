# 使用你的验证器

你的验证器可用于为函数和类添加值检查功能。例如，也许这些验证器可用于 `Stock` 的属性中：

```python
class Stock:
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)
  ...
```

从 `stock.py` 复制 `Stock` 类，并修改它，使其在 `shares` 和 `price` 的属性代码中使用验证器。
