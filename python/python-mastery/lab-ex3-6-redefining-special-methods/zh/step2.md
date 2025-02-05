# 使对象具有可比性

如果你创建两个相同的 `Stock` 对象并尝试比较它们，会发生什么？试试看：

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
False
>>>
```

你可以通过为 `Stock` 类提供一个 `__eq__()` 方法来解决这个问题。例如：

```python
class Stock:
  ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
  ...
```

进行此更改后，再次尝试比较两个对象。
