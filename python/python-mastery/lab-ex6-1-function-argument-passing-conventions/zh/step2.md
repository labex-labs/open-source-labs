# 简化的数据结构

在之前的实验中，你定义了一个表示股票的类，如下所示：

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

关注一下`__init__()`方法 —— 每次你想要填充一个结构时，这不是要键入很多代码吗？要是你必须在程序中定义几十个这样的结构呢？

在一个名为`structure.py`的文件中，定义一个基类`Structure`，它允许用户按如下方式定义简单的数据结构：

```python
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year','month', 'day')
```

`Structure`类应该定义一个`__init__()`方法，该方法接受任意数量的参数，并查找是否存在`_fields`类变量。让该方法根据`_fields`中的属性名和传递给`__init__()`的参数来填充实例。

以下是一些测试你实现的示例代码：

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s = Stock('AA',50)
Traceback (most recent call last):
...
TypeError: Expected 3 arguments
>>>
```
