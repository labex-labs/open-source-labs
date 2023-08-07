# Enforcing Validation Rules

Using properties and private attributes, modify the `shares` attribute of the `Stock` class so that it can only be assigned a non-negative integer value. In addition, modify the `price` attribute so that it can only be assigned a non-negative floating point value.

The new object should work almost exactly the same as the old one except for extra type and value checking.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.shares = 50          # OK
>>> s.shares = '50'
Traceback (most recent call last):
...
TypeError: Expected integer
>>> s.shares = -10
Traceback (most recent call last):
...
ValueError: shares must be >= 0

>>> s.price = 123.45       # OK
>>> s.price = '123.45'
Traceback (most recent call last):
...
TypeError: Expected float
>>> s.price = -10.0
Traceback (most recent call last):
...
ValueError: price must be >= 0
>>>
```
