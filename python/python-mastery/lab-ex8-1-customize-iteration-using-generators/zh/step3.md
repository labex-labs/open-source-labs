# 迭代的惊人力量

Python 使用迭代的方式可能出乎你的意料。一旦你在 `Structure` 类中添加了 `__iter__()`，你会发现很容易执行各种新操作。例如，转换为序列和解包：

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> list(s)
['GOOG', 100, 490.1]
>>> tuple(s)
('GOOG', 100, 490.1)
>>> name, shares, price = s
>>> name
'GOOG'
>>> shares
100
>>> price
490.1
>>>
```

既然说到这里，我们现在可以为 `Structure` 类添加一个比较运算符：

```python
# structure.py
class Structure(metaclass=StructureMeta):
 ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
 ...
```

现在你应该能够比较对象了：

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
True
>>>
```

再次运行你的 `teststock.py` 单元测试。现在所有测试应该都能通过了。太棒了。
