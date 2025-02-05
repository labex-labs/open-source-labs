# 数学运算符

如果你为对象实现了适当的方法，就可以使其与各种数学运算符一起使用。然而，识别其他类型的数据并实现适当的转换代码是你的责任。通过为 `MutInt` 类添加一个 `__add__()` 方法来修改它，如下所示：

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
```

有了这个改变，你会发现你既可以将整数与可变整数相加。结果是一个 `MutInt` 实例。将 `MutInt` 与其他类型的数字相加会导致错误：

```python
>>> a = MutInt(3)
>>> b = a + 10
>>> b
MutInt(13)
>>> b.value = 23
>>> c = a + b
>>> c
MutInt(26)
>>> a + 3.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'float'
>>>
```

这段代码存在一个问题，当操作数的顺序颠倒时它就不起作用了。考虑以下情况：

```python
>>> a + 10
MutInt(13)
>>> 10 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'MutInt'
>>>
```

这是因为 `int` 类型不了解 `MutInt`，所以它感到困惑。可以通过添加一个 `__radd__()` 方法来解决这个问题。如果第一次尝试调用 `__add__()` 时对提供的对象不起作用，就会调用这个方法。

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__    # 操作数颠倒
```

有了这个改变，你会发现加法运算可以正常工作了：

```python
>>> a = MutInt(3)
>>> a + 10
MutInt(13)
>>> 10 + a
MutInt(13)
>>>
```

由于我们的整数是可变的，你还可以通过实现 `__iadd__()` 方法，使其识别就地加更新运算符 `+=`：

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

这允许进行如下有趣的使用：

```python
>>> a = MutInt(3)
>>> b = a
>>> a += 10
>>> a
MutInt(13)
>>> b                 # 注意 b 也改变了
MutInt(13)
>>>
```

`b` 也改变了，这可能看起来有点奇怪，但内置的 Python 对象有这样的微妙特性。例如：

```python
>>> a = [1,2,3]
>>> b = a
>>> a += [4,5]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]

>>> c = (1,2,3)
>>> d = c
>>> c += (4,5)
>>> c
(1, 2, 3, 4, 5)
>>> d                  # 解释与列表的区别
(1, 2, 3)
>>>
```
