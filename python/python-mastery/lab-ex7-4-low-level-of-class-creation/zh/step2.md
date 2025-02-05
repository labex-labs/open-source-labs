# 带类型的结构体

在 `structure.py` 文件中，定义以下函数：

```python
# structure.py

...
def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
```

这个函数在某种程度上类似于 `namedtuple()` 函数，因为它创建了一个类。试试看：

```python
>>> from validate import String, PositiveInteger, PositiveFloat
>>> from structure import typed_structure
>>> Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

你可能会发现自己的脑袋现在开始有点发懵了。
