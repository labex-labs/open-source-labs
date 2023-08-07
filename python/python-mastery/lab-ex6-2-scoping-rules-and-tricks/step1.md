# Preparation

In the last exercise, you create a class `Structure` that made it easy to define data structures. For example:

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

This works fine except that a lot of things are pretty weird about the `__init__()` function. For example, if you ask for help using `help(Stock)`, you don't get any kind of useful signature. Also, keyword argument passing doesn't work. For example:

```python
>>> help(Stock)
... look at output ...

>>> s = Stock(name='GOOG', shares=100, price=490.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() got an unexpected keyword argument 'price'
>>>
```

In this exercise, we're going to look at a different approach to the problem.
