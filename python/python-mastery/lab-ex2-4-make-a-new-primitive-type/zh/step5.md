# 转换

你新创建的原始类型已基本完成。你可能希望赋予它进行一些常见转换的能力。例如：

```python
>>> a = MutInt(3)
>>> int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>> float(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>>
```

你可以为你的类添加一个 `__int__()` 和 `__float__()` 方法来解决这个问题：

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
```

现在，你可以正确地进行转换了：

```python
>>> a = MutInt(3)
>>> int(a)
3
>>> float(a)
3.0
>>>
```

一般来说，Python 不会自动进行数据转换。因此，即使你为类添加了 `__int__()` 方法，在某些预期为整数的情况下，`MutInt` 仍然无法正常工作。例如，索引操作：

```python
>>> names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
>>> a = MutInt(1)
>>> names[a]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not MutInt
>>>
```

可以通过为 `MutInt` 添加一个返回整数的 `__index__()` 方法来解决这个问题。像这样修改类：

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    __index__ = __int__     # 使索引操作生效
```

**讨论**

在 Python 中创建一个新的原始数据类型实际上是最复杂的编程任务之一。有很多边界情况和底层问题需要考虑——特别是关于你的类型如何与其他 Python 类型交互。可能需要牢记的关键一点是，如果你了解底层协议，就可以自定义对象与 Python 其他部分交互的几乎每个方面。如果你要这样做，建议查看现有代码中与你试图创建的类似的内容。
