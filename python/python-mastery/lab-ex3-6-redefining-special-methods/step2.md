# Making objects comparable

What happens if you create two identical `Stock` objects and try to compare them? Find out:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
False
>>>
```

You can fix this by giving the `Stock` class an `__eq__()` method. For example:

```python
class Stock:
    ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
    ...
```

Make this change and try comparing two objects again.
