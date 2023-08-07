# Adding `__slots__`

Modify your new `Stock` class to use `__slots__`. You will find that you have to use a different set of attribute names than before--specifically, you will have to list the private attribute names (e.g., if a property is storing a value in an attribute `_shares`, that is the name you list in `__slots__`). Verify that the class still works and that you can no longer add new attributes.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.spam = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Stock' object has no attribute 'spam'
>>>
```
