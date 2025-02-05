# 作为代码生成器的闭包

在练习4.3中，你开发了一组描述符类，用于对对象属性进行类型检查。例如：

```python

class Stock:
    name = String()
    shares = Integer()
    price = Float()
```

这种功能也可以使用闭包来实现。创建一个名为`typedproperty.py`的文件，并在其中放入以下代码：

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

这看起来很奇特，但这个函数实际上是在生成代码。你可以在类定义中这样使用它：

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

验证这个类是否与描述符代码一样进行类型检查。

在`typedproperty.py`文件中添加函数`String()`、`Integer()`和`Float()`，这样你就可以编写以下代码：

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```
