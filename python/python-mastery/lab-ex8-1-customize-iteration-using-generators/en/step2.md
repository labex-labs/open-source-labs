# Adding Iteration to Objects

If you've created a custom class, you can make it support iteration by defining an `__iter__()` special method. `__iter__()` returns an iterator as a result. As shown in the previous example, an easy way to do it is to define `__iter__()` as a generator.

In earlier exercises, you defined a `Structure` base class. Add an `__iter__()` method to this class that produces the attribute values in order. For example:

```python
class Structure(metaclass=StructureMeta):
    ...
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
    ...
```

Once you've done this, you should be able to iterate over the instance attributes like this:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> for val in s:
        print(val)
GOOG
100
490.1
>>>
```
