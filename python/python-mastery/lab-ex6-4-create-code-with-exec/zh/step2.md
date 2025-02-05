# 创建一个 `__init__()` 函数

在练习 6.3 中，你编写了代码来检查 `__init__()` 方法的签名，以便在 `_fields` 类变量中设置属性名称。例如：

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

Stock.set_fields()
```

不要检查 `__init__()` 方法，而是编写一个类方法 `create_init(cls)`，它根据 `_fields` 的值创建一个 `__init__()` 方法。使用 `exec()` 函数来实现这一点，就像上面展示的那样。以下是用户使用它的方式：

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')

Stock.create_init()
```

生成的类应该与之前的工作方式完全相同：

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

按照所示修改正在处理的 `Stock` 类，以使用 `create_init()` 函数。像之前一样用单元测试进行验证。

在做这件事的同时，去掉 `Structure` 类上的 `_init()` 和 `set_fields()` 方法——那种方法有点奇怪。
