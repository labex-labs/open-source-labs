# Iteration over a sequence

The for-loop iterates over the elements in a sequence.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

On each iteration of the loop, you get a new item to work with.
This new value is placed into the iteration variable. In this example, the
iteration variable is `x`:

```python
for x in s:         # `x` is an iteration variable
    ...statements
```

On each iteration, the previous value of the iteration variable is overwritten (if any).
After the loop finishes, the variable retains the last value.
