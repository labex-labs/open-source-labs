# 创建大量类

在其他一些情况下，直接使用 `type()` 构造函数可能会更有优势。看看这段代码：

```python
# validate.py
...

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'expected {cls.expected_type}')
        super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
...
```

哇，最后一部分既烦人又重复。把它改成使用一个期望类型类的表，如下所示：

```python
# validate.py
...

_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String','str') ]

globals().update((name, type(name, (Typed,), {'expected_type':ty}))
                 for name, ty in _typed_classes)
```

现在，如果你想有更多的类型类，只需要把它们添加到表中：

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('Complex', complex),
    ('Decimal', decimal.Decimal),
    ('List', list),
    ('Bool', bool),
    ('String','str') ]
```

承认吧，这有点酷，还能节省很多键盘输入。
