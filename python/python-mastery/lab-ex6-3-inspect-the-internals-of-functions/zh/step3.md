# 整合起来

在练习6.1中，你创建了一个类 `Structure`，它定义了通用的 `__init__()`、`__setattr__()` 和 `__repr__()` 方法。该类要求用户像这样定义一个 `_fields` 类变量：

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

这个类的问题在于，就帮助文档和关键字参数传递而言，`__init__()` 函数没有一个有用的参数签名。在练习6.2中，你使用了一个涉及特殊的 `self._init()` 函数的巧妙技巧。例如：

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')
    def __init__(self, name, shares, price):
        self._init()
  ...
```

这给出了一个有用的签名，但现在这个类变得很奇怪，因为用户必须同时提供 `_fields` 变量和 `__init__()` 方法。

你的任务是使用一些函数检查技术来消除 `_fields` 变量。首先，注意你可以如下从 `Stock` 中获取参数签名：

```python
>>> import inspect
>>> sig = inspect.signature(Stock)
>>> tuple(sig.parameters)
('name','shares', 'price')
>>>
```

也许你可以根据 `__init__()` 的参数签名来设置 `_fields` 变量。向 `Structure` 添加一个类方法 `set_fields(cls)`，它检查 `__init__()` 函数，并适当地设置 `_fields` 变量。你应该像这样使用你的新函数：

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

  ...

Stock.set_fields()
```

结果类的工作方式应该与以前相同：

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

再次使用你的单元测试来验证稍微修改后的 `Stock` 类。仍然会有失败情况，但与上一个练习相比应该没有什么变化。

此时，这一切仍然有点“棘手”，但你正在取得进展。你有一个具有有用的 `__init__()` 函数的股票结构类，有一个有用的表示字符串，并且 `__setattr__()` 方法限制了属性名的集合。必须调用 `set_fields()` 这一额外步骤有点奇怪，但我们稍后再处理这个问题。
