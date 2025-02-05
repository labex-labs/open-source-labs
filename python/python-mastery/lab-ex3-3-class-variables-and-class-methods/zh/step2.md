# 替代构造函数

或许通过一个替代构造函数来处理从一行原始数据创建 `Stock` 实例会更好。修改 `Stock` 类，使其具有一个 `types` 类变量和一个 `from_row()` 类方法，如下所示：

```python
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
  ...
```

以下是测试它的方法：

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock.from_row(row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>> s.cost()
3220.0000000000005
>>>
```

仔细观察这一行中的字符串值是如何被转换为正确类型的。
