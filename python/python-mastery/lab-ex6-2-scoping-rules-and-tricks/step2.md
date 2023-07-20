# Show me your locals

First, try an experiment by defining the following class:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            print(locals())

>>>
```

Now, try running this:

```python
>>> s = Stock('GOOG', 100, 490.1)
{'self': <__main__.Stock object at 0x100699b00>, 'price': 490.1, 'name': 'GOOG', 'shares': 100}
>>>
```

Notice how the locals dictionary contains all of the arguments passed
to `__init__()`. That's interesting. Now, define the following function
and class definitions:

```python
>>> def _init(locs):
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

>>> class Stock:
        def __init__(self, name, shares, price):
            _init(locals())
```

In this code, the `_init()` function is used to automatically
initialize an object from a dictionary of passed local variables.
You'll find that `help(Stock)` and keyword arguments work perfectly.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>>
```
