# Bound Methods

It may be surprising, but method calls are layered onto the machinery used
for simple attributes. Essentially, a method is an attribute that
executes when you add the required parentheses () to call it like a function. For
example:

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.cost           # Looks up the method
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> s.cost()         # Looks up and calls the method
49010.0

>>> # Same operations using getattr()
>>> getattr(s, 'cost')
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> getattr(s, 'cost')()
49010.0
>>>
```

A bound method is attached to the object where it came from. If that
object is modified, the method will see the modifications. You can
view the original object by inspecting the `__self__` attribute
of the method.

```python
>>> c = s.cost
>>> c()
49010.0
>>> s.shares = 75
>>> c()
36757.5
>>> c.__self__
<__main__.Stock object at 0x409530>
>>> c.__func__
<function cost at 0x37cc30>
>>> c.__func__(c.__self__)      # This is what happens behind the scenes of calling c()
36757.5
>>>
```

Try it with the `sell()` method just to make sure you
understand the mechanics:

```python
>>> f = s.sell
>>> f.__func__(f.__self__, 25)     # Same as s.sell(25)
>>> s.shares
50
>>>
```
