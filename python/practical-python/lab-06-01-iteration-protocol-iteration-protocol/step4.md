# Exercise 6.1: Iteration Illustrated

Create the following list:

```python
a = [1,9,4,25,16]
```

Manually iterate over this list. Call `__iter__()` to get an iterator and call the `__next__()` method to obtain successive elements.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

The `next()` built-in function is a shortcut for calling the `__next__()` method of an iterator. Try using it on a file:

```python
>>> f = open('Data/portfolio.csv')
>>> f.__iter__()    # Note: This returns the file itself
<_io.TextIOWrapper name='Data/portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

Keep calling `next(f)` until you reach the end of the file. Watch what happens.
