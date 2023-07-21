# Iteration: Protocol

Consider the `for`-statement.

```python
for x in obj:
    # statements
```

What happens under the hood?

```python
_iter = obj.__iter__()        # Get iterator object
while True:
    try:
        x = _iter.__next__()  # Get next item
        # statements ...
    except StopIteration:     # No more items
        break
```

All the objects that work with the `for-loop` implement this low-level
iteration protocol.

Example: Manual iteration over a list.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```
