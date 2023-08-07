# The Surprising Power of Iteration

Python uses iteration in ways you might not expect. Once you've added `__iter__()` to the `Structure` class, you'll find that it is easy to do all sorts of new operations. For example, conversions to sequences and unpacking:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> list(s)
['GOOG', 100, 490.1]
>>> tuple(s)
('GOOG', 100, 490.1)
>>> name, shares, price = s
>>> name
'GOOG'
>>> shares
100
>>> price
490.1
>>>
```

While we're at it, we can now add a comparison operator to our `Structure` class:

```python
# structure.py
class Structure(metaclass=StructureMeta):
    ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
    ...
```

You should now be able to compare objects:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
True
>>>
```

Try running your `teststock.py` unit tests again. Everything should be passing now. Excellent.
