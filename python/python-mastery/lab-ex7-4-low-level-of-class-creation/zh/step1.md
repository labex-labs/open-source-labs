# 创建类

回顾一下，在之前的实验中，我们定义了一个简单的类 `Stock`，如下所示：

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares
```

我们在这里要做的是手动创建这个类。首先像定义普通 Python 函数一样定义这些方法。

```python
>>> def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

>>> def cost(self):
        return self.shares*self.price

>>> def sell(self,nshares):
        self.shares -= nshares

>>>
```

接下来，创建一个方法字典：

```python
>>> methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell }

>>>
```

最后，创建 `Stock` 类对象：

```python
>>> Stock = type('Stock',(object,),methods)
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>> s.sell(25)
>>> s.shares
75
>>>
```

恭喜你，你刚刚创建了一个类。一个类实际上只不过是一个名称、一个基类元组以及一个包含所有类内容的字典。`type()` 是一个构造函数，如果你提供这三个部分，它会为你创建一个类。
