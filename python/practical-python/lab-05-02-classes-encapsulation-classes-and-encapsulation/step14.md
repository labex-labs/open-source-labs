# Exercise 5.8: Adding slots

Modify the `Stock` class so that it has a `__slots__` attribute. Then,
verify that new attributes can't be added:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.blah = 42
... see what happens ...
>>>
```

When you use `__slots__`, Python uses a more efficient
internal representation of objects. What happens if you try to
inspect the underlying dictionary of `s` above?

```python
>>> s.__dict__
... see what happens ...
>>>
```

It should be noted that `__slots__` is most commonly used as an
optimization on classes that serve as data structures. Using slots
will make such programs use far-less memory and run a bit faster.
You should probably avoid `__slots__` on most other classes however.
