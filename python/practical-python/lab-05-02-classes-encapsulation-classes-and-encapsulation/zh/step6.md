# 托管属性

一种方法：引入访问器方法。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # 实现“获取”操作的函数
    def get_shares(self):
        return self._shares

    # 实现“设置”操作的函数
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
```

糟糕的是，这会破坏我们所有现有的代码。`s.shares = 50` 变成了 `s.set_shares(50)`
