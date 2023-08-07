# List growth

Python lists are highly optimized for performing `append()`
operations. Each time a list grows, it grabs a larger chunk of memory
than it actually needs with the expectation that more data will be
added to the list later. If new items are added and space is
available, the `append()` operation stores the item without
allocating more memory.

Experiment with this feature of lists by using
the `sys.getsizeof()` function on a list and appending a few
more items.

```python
>>> import sys
>>> items = []
>>> sys.getsizeof(items)
64
>>> items.append(1)
>>> sys.getsizeof(items)
96
>>> items.append(2)
>>> sys.getsizeof(items)    # Notice how the size does not increase
96
>>> items.append(3)
>>> sys.getsizeof(items)    # It still doesn't increase here
96
>>> items.append(4)
>>> sys.getsizeof(items)    # Not yet.
96
>>> items.append(5)
>>> sys.getsizeof(items)    # Notice the size has jumped
128
>>>
```

A list stores its items by reference. So, the memory required for
each item is a single memory address. On a 64-bit machine, an address
is typically 8 bytes. However, if Python has been compiled for
32-bits, it might be 4 bytes and the numbers for the above example
will be half of what's shown.
