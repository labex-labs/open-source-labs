# 从验证器到描述符

在之前的练习中，你编写了一系列能够执行检查的类。例如：

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError('Expected %s' % cls.expected_type)
TypeError: 预期为 <class 'int'>
>>> PositiveInteger.check(-10)
```

你可以通过对`Validator`基类进行简单修改，将其扩展为描述符。将其修改如下：

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

注意：描述符中缺少`__get__()`方法意味着Python将使用其默认的属性查找实现。这要求提供的名称与实例字典中使用的名称匹配。

无需进行其他更改。现在，尝试修改`Stock`类，使其像这样将验证器用作描述符：

```python
class Stock:
    name   = String('name')
    shares = PositiveInteger('shares')
    price  = PositiveFloat('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

你会发现你的类的工作方式与之前相同，代码量大大减少，并且提供了所有所需的检查：

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.shares = 75
>>> s.shares = '75'
... 类型错误...
>>> s.shares = -50
... 值错误...
>>>
```

这非常酷。描述符使你能够极大地简化`Stock`类的实现。这就是描述符的真正强大之处——你可以对点运算符进行底层控制，并利用它来实现惊人的功能。
