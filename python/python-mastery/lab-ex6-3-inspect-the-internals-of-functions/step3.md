# Putting it Together

In Exercise 6.1, you created a class `Structure` that defined a generalized `__init__()`, `__setattr__()`, and `__repr__()` method. That class required a user to define a `_fields` class variable like this:

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

The problem with this class is that the `__init__()` function didn't have a useful argument signature for the purposes of help and keyword argument passing. In Exercise 6.2, you did a sneaky trick involving a special `self._init()` function. For example:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    def __init__(self, name, shares, price):
        self._init()
    ...
```

This gave a useful signature, but now the class is just weird because the user has to provide both the `_fields` variable and the `__init__()` method.

Your task is to eliminate the `_fields` variable using some function inspection techniques. First, notice that you can get the argument signature from `Stock` as follows:

```python
>>> import inspect
>>> sig = inspect.signature(Stock)
>>> tuple(sig.parameters)
('name', 'shares', 'price')
>>>
```

Perhaps you could set the `_fields` variable from the argument signature of `__init__()`. Add a class method `set_fields(cls)` to `Structure` that inspects the `__init__()` function, and sets the `_fields` variable appropriately. You should use your new function like this:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

    ...

Stock.set_fields()
```

The resulting class should work the same way as before:

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

Verify the slightly modified `Stock` class with your unit tests again. There will still be failures, but nothing should change from the previous exercise.

At this point, it's all still a bit "hacky", but you're making progress. You have a Stock structure class with a useful `__init__()` function, there is a useful representation string, and the `__setattr__()` method restricts the set of attribute names. The extra step of having to invoke `set_fields()` is a bit odd, but we'll get back to that.
