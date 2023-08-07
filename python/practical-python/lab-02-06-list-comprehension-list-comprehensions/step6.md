# Exercise 2.19: List comprehensions

Try a few simple list comprehensions just to become familiar with the syntax.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

Notice how the list comprehensions are creating a new list with the data suitably transformed or filtered.
