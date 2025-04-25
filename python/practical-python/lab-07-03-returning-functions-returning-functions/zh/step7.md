# 练习 7.7：使用闭包避免重复

闭包更强大的特性之一是其在生成重复代码方面的应用。如果你回顾一下练习 5.7，还记得用于定义带类型检查的属性的代码。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
  ...
```

你无需一遍又一遍地重复输入这段代码，而是可以使用闭包自动创建它。

创建一个名为`typedproperty.py`的文件，并将以下代码放入其中：

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

现在，通过定义如下类来试用一下：

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

尝试创建一个实例并验证类型检查是否有效。

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... 应该会得到一个TypeError...
>>>
```
