# 字符串转换的特殊方法

对象有两种字符串表示形式。

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

`str()` 函数用于创建美观的可打印输出：

```python
>>> str(d)
'2012-12-21'
>>>
```

`repr()` 函数用于为程序员创建更详细的表示形式。

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

`str()` 和 `repr()` 这两个函数在类中使用一对特殊方法来生成要显示的字符串。

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 与 `str()` 一起使用
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # 与 `repr()` 一起使用
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_注意：`__repr__()` 的约定是返回一个字符串，当将其输入到 `eval()` 中时，将重新创建底层对象。如果无法做到这一点，则使用某种易于阅读的表示形式代替。_
