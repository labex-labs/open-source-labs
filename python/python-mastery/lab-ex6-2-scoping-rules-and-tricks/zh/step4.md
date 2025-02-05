# 整合

结合前两部分的思路，删除最初作为 `Structure` 类一部分的 `__init__()` 方法。接下来，添加一个如下所示的 `_init()` 方法：

```python
# structure.py
import sys

class Structure:
  ...
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
  ...
```

注意：将其定义为 `@staticmethod` 的原因是 `self` 参数是从局部变量中获取的 —— 无需再将其作为参数额外传递给方法本身（诚然，这有点微妙）。

现在，修改你的 `Stock` 类，使其如下所示：

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares
```

验证该类是否正常工作，是否支持关键字参数，以及是否具有正确的帮助签名。

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>> help(Stock)
... 查看输出...
>>>
```

再次运行 `teststock.py` 中的单元测试。你应该会看到至少又有一个测试通过。太棒了！

此时，看起来我们好像倒退了一大步。不仅类需要 `__init__()` 方法，它们还需要 `_fields` 变量才能使其他一些方法正常工作（`__repr__()` 和 `__setattr__()`）。此外，使用 `self._init()` 看起来相当棘手。我们会解决这个问题的，耐心点。
