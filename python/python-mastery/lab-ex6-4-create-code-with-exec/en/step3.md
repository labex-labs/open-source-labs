# Named Tuples

In Exercise 2.1, you experimented with `namedtuple` objects in the `collections` module. Just to refresh your memory, here is how they worked:

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name', 'shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]
100
>>>
```

Under the covers, the `namedtuple()` function is creating code as a string and executing it using `exec()`. Look at the code and marvel:

```python
>>> import inspect
>>> print(inspect.getsource(namedtuple))
... look at the output ...
>>>
```
