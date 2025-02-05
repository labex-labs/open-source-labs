# 使用类装饰器来填充细节

上述代码中一个令人烦恼的方面是存在一些额外的细节，比如`_fields`变量以及`Stock.create_init()`的最后一步。很多这些内容可以打包到一个类装饰器中。

在`structure.py`文件中，创建一个类装饰器`@validate_attributes`，它会检查类体中是否有`Validator`的实例，并填充`_fields`变量。例如：

```python
# structure.py

from validate import Validator

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    return cls
```

这段代码依赖于Python 3.6开始类字典是有序的这一事实。因此，它会按照列出的顺序遇到不同的`Validator`描述符。利用这个顺序，你就可以填充`_fields`变量。这样你就可以编写如下代码：

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
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

一旦你让这个功能正常工作，修改`@validate_attributes`装饰器，使其额外执行调用`Stock.create_init()`的最后一步。这样类就可以简化为如下形式：

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
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
