# 使用 `__slots__` 与 `__setattr__` 的对比

在之前的练习中，`__slots__` 用于列出类的实例属性。使用 `__slots__` 的主要目的是优化内存使用。其次要作用是将允许的属性严格限制为所列出的那些属性。使用 `__slots__` 的一个缺点是它常常与 Python 的其他部分产生奇怪的交互（例如，使用 `__slots__` 的类不能用于多重继承）。因此，除非在特殊情况下，否则真的不应该使用 `__slots__`。

如果你真的想限制允许的属性集，另一种方法是定义一个 `__setattr__()` 方法。试试这个实验：

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def __setattr__(self, name, value):
            if name not in { 'name','shares', 'price' }:
                raise AttributeError('No attribute %s' % name)
            super().__setattr__(name, value)

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares = 75
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: No attribute share
>>>
```

在这个例子中，没有使用 `__slots__`，但 `__setattr__()` 方法仍然将属性限制为预定义集合中的那些属性。你可能需要思考这种方法与继承的交互方式（例如，如果子类想要添加新属性，它们可能需要重新定义 `__setattr__()` 以使其正常工作）。
