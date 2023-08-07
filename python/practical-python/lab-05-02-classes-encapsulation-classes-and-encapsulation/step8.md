# Uniform access

The last example shows how to put a more uniform interface on an object. If you don't do this, an object might be confusing to use:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> a = s.cost() # Method
49010.0
>>> b = s.shares # Data attribute
100
>>>
```

Why is the `()` required for the cost, but not for the shares? A property can fix this.
