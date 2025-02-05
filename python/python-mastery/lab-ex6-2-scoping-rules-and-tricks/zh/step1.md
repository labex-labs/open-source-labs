# 准备工作

在上一个练习中，你创建了一个 `Structure` 类，它使得定义数据结构变得很容易。例如：

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')
```

这样做没问题，只是 `__init__()` 函数存在很多奇怪的地方。例如，如果你使用 `help(Stock)` 来获取帮助，你不会得到任何有用的签名信息。此外，通过关键字参数传递也不起作用。例如：

```python
>>> help(Stock)
... 查看输出...

>>> s = Stock(name='GOOG', shares=100, price=490.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() got an unexpected keyword argument 'price'
>>>
```

在这个练习中，我们将研究解决这个问题的另一种方法。
