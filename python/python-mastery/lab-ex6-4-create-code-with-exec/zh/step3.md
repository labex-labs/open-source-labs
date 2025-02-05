# 具名元组

在练习 2.1 中，你尝试过 `collections` 模块中的具名元组（`namedtuple`）对象。为了帮你回忆一下，下面是它们的工作方式：

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name','shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]
100
>>>
```

在底层，`namedtuple()` 函数会将代码创建为字符串，并使用 `exec()` 来执行它。看看这段代码，惊叹一下吧：

```python
>>> import inspect
>>> print(inspect.getsource(namedtuple))
... 看看输出结果...
>>>
```
