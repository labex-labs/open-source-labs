# Special methods for String Conversions

Objects have two string representations.

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

The `str()` function is used to create a nice printable output:

```python
>>> str(d)
'2012-12-21'
>>>
```

The `repr()` function is used to create a more detailed representation for programmers.

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

Those functions, `str()` and `repr()`, use a pair of special methods in the class to produce the string to be displayed.

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Used with `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_Note: The convention for `__repr__()` is to return a string that, when fed to `eval()`, will recreate the underlying object. If this is not possible, some kind of easily readable representation is used instead._
