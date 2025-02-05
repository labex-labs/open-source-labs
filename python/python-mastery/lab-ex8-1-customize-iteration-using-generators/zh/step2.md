# 为对象添加迭代功能

如果你创建了一个自定义类，那么可以通过定义一个 `__iter__()` 特殊方法来使其支持迭代。`__iter__()` 返回一个迭代器。如前一个示例所示，一种简单的做法是将 `__iter__()` 定义为一个生成器。

在之前的练习中，你定义了一个 `Structure` 基类。为这个类添加一个 `__iter__()` 方法，使其按顺序生成属性值。例如：

```python
class Structure(metaclass=StructureMeta):
  ...
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
  ...
```

完成此操作后，你应该能够像这样遍历实例属性：

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> for val in s:
        print(val)
GOOG
100
490.1
>>>
```
