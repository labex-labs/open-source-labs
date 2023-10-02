# Bound Methods

A method that has not yet been invoked by the function call operator `()` is known as a _bound method_. It operates on the instance where it originated.

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

Bound methods are often a source of careless non-obvious errors. For example:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

Or devious behavior that's hard to debug.

```python
f = open(filename, 'w')
...
f.close     # Oops, Didn't do anything at all. `f` still open.
```

In both of these cases, the error is cause by forgetting to include the trailing parentheses. For example, `s.cost()` or `f.close()`.
