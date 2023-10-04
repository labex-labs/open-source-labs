# Debugging with Print

`print()` debugging is quite common.

_Tip: Make sure you use `repr()`_

```python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()` shows you an accurate representation of a value. Not the _nice_ printing output.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# NO `repr`
>>> print(x)
3.4
# WITH `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
   