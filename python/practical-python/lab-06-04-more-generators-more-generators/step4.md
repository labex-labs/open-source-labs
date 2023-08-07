# Exercise 6.13: Generator Expressions

Generator expressions are a generator version of a list comprehension. For example:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x109207e60>
>>> for n in squares:
...     print(n)
...
1
4
9
16
25
```

Unlike a list a comprehension, a generator expression can only be used once. Thus, if you try another for-loop, you get nothing:

```python
>>> for n in squares:
...     print(n)
...
>>>
```
