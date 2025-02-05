# 重新审视描述符

在实验4.3中，你定义了一些描述符，允许用户定义具有类型检查属性的类，如下所示：

```python
from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
 ...
```

修改你的`Stock`类，使其包含上述描述符，现在看起来像这样（见实验6.4）：

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name','shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```

运行`teststock.py`中的单元测试。添加类型检查后，你应该会看到大量测试通过。很棒。
