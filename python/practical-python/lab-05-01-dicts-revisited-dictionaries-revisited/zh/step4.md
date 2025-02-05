# 类成员（Class Member）

还有一个独立的字典用于保存方法。

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

这个字典存储在 `Stock.__dict__` 中。

```python
{
    'cost': <function>,
    'sell': <function>,
    '__init__': <function>
}
```
