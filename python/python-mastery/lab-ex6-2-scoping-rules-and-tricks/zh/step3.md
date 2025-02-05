# 栈帧破解

对于上一部分内容，有人可能会抱怨说，在 `__init__()` 函数中插入对 `locals()` 的调用后，它看起来相当怪异。不过，如果你愿意进行一些栈帧破解，就可以解决这个问题。试试 `_init()` 函数的这个变体：

```python
>>> import sys
>>> def _init():
        locs = sys._getframe(1).f_locals   # 获取调用者的局部变量
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
>>>
```

在这段代码中，局部变量是从调用者的栈帧中提取的。下面是修改后的类定义：

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            _init()

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

此时，你可能会感到相当不安。没错，你刚刚编写了一个函数，它深入到另一个函数的栈帧中并检查其局部变量。
