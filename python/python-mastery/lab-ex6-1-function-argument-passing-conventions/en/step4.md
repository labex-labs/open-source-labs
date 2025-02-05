# Restricting Attribute Names

Give the `Structure` class a `__setattr__()` method that restricts the allowed set of attributes to those listed in the `_fields` variable. However, it should still allow any "private" attribute (e.g., name starting with `_` to be set).

For example:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 13, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>> s._shares = 100     # Private attribute. OK
>>>
```
