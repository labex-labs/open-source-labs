# 通过继承应用装饰器

必须指定类装饰器本身有点麻烦。使用以下`__init_subclass__()`方法修改`Structure`类：

```python
# structure.py

class Structure:
  ...
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

做出此更改后，你应该能够完全去掉装饰器，仅依靠继承。这是继承加上一些隐藏的魔法！

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

    def sell(self, nshares):
        self.shares -= nshares
```

现在，代码真的开始有进展了。事实上，它看起来几乎很正常了。让我们继续推进。
