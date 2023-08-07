# Slots vs. setattr

In previous exercises, `__slots__` was used to list the instance attributes on a class. The primary purpose of slots is to optimize the use of memory. A secondary effect is that it strictly limits the allowed attributes to those listed. A downside of slots is that it often interacts strangely with other parts of Python (for example, classes using slots can't be used with multiple inheritance). For that reason, you really shouldn't use slots except in special cases.

If you really wanted to limit the set of allowed attributes, an alternate way to do it would be to define a `__setattr__()` method. Try this experiment:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def __setattr__(self, name, value):
            if name not in { 'name', 'shares', 'price' }:
                raise AttributeError('No attribute %s' % name)
            super().__setattr__(name, value)

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares = 75
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: No attribute share
>>>
```

In this example, there are no slots, but the `__setattr__()` method still restricts attributes to those in a predefined set. You'd probably need to think about how this approach might interact with inheritance (e.g., if subclasses wanted to add new attributes, they'd probably need to redefine `__setattr__()` to make it work).
