# Creating an `__init__()` function

In Exercise 6.3, you wrote code that inspected the signature of the `__init__()` method to set the attribute names in a `_fields` class variable. For example:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

Stock.set_fields()
```

Instead of inspecting the `__init__()` method, write a class method `create_init(cls)` that creates an `__init__()` method from the value of `_fields`. Use the `exec()` function to do this as shown above. Here's how a user will use it:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

Stock.create_init()
```

The resulting class should work exactly the name way as before:

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

Modify the `Stock` class in progress to use the `create_init()` function as shown.\
Verify with your unit tests as before.

While you're at it, get rid of the `_init()` and `set_fields()` methods on the `Structure` class--that approach was kind of weird.
