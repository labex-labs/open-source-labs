# 看看你的局部变量

首先，通过定义以下类来做一个实验：

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            print(locals())

>>>
```

现在，试着运行这个：

```python
>>> s = Stock('GOOG', 100, 490.1)
{'self': <__main__.Stock object at 0x100699b00>, 'price': 490.1, 'name': 'GOOG','shares': 100}
>>>
```

注意局部变量字典是如何包含所有传递给 `__init__()` 的参数的。这很有意思。现在，定义以下函数和类定义：

```python
>>> def _init(locs):
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

>>> class Stock:
        def __init__(self, name, shares, price):
            _init(locals())
```

在这段代码中，`_init()` 函数用于根据传递的局部变量字典自动初始化一个对象。你会发现 `help(Stock)` 和关键字参数都能完美工作。

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>>
```
