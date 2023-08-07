# Generator Expressions

A generator expression is almost exactly the same as a list comprehension except that it does not create a list. Instead, it creates an object that produces the results incrementally--typically for consumption by iteration. Try a simple example:

```python
>>> nums = [1,2,3,4,5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x37caa8>
>>> for n in squares:
        print(n)

1
4
9
16
25
>>>
```

You will notice that a generator expression can only be used once. Watch what happens if you do the for-loop again:

```python
>>> for n in squares:
         print(n)

>>>
```

You can manually get the results one-at-a-time if you use the `next()` function. Try this:

```python
>>> squares = (x*x for x in nums)
>>> next(squares)
1
>>> next(squares)
4
>>> next(squares)
9
>>>
```

Keeping typing `next()` to see what happens when there is no more data.

If the task you are performing is more complicated, you can still take advantage of generators by writing a generator function and using the `yield` statement instead. For example:

```python
>>> def squares(nums):
        for x in nums:
            yield x*x

>>> for n in squares(nums):
        print(n)

1
4
9
16
25
>>>
```

We'll return to generator functions a little later in the course--for now, just view such functions as having the interesting property of feeding values to the `for`-statement.
