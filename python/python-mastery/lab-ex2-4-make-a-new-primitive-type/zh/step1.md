# 可变整数

Python 中的整数通常是不可变的。然而，假设你想要创建一个可变的整数对象。首先创建一个这样的类：

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

试试看：

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt object at 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'int'
>>>
```

这一切看起来都很有趣，只是这个新的 `MutInt` 对象实际上没什么用。打印效果很糟糕，所有的数学运算符都不能用，基本上没什么实际用途。嗯，除了它的值是可变的这一点——它确实有这个特性。
