# 方法参数检查

还记得你在上一部分编写的`@validated`装饰器吗？让我们修改`@validate_attributes`装饰器，以便类中任何带有注释的方法都能自动被`@validated`包装。这使你能够在诸如`sell()`方法等方法上添加强制注释：

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

你会发现`sell()`现在会对参数进行强制检查。

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.sell(-25)
Traceback (most recent call last):
...
TypeError: Bad Arguments
  nshares: must be >= 0
>>>
```

是的，现在这开始变得非常有趣了。类装饰器和继承的结合是一股强大的力量。
