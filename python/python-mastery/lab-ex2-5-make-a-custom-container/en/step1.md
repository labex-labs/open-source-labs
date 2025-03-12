# Understanding List Memory Allocation

Python lists are designed to be efficient for appending operations. Instead of allocating exactly the amount of memory needed, Python allocates extra memory in anticipation of future additions. This strategy minimizes the number of memory reallocations needed when the list grows.

Let's examine this behavior using the `sys.getsizeof()` function, which returns the size of an object in bytes.

1. Open a Python interactive shell in your terminal:

```bash
python3
```

2. Import the `sys` module and create an empty list:

```python
import sys
items = []
```

3. Check the initial size of the empty list:

```python
sys.getsizeof(items)
```

You should see a value like `64` bytes, which represents the overhead for an empty list.

4. Now, let's add items to the list one by one and observe how the memory allocation changes:

```python
items.append(1)
sys.getsizeof(items)
```

You should see a larger value, around `96` bytes.

5. Continue adding more items and check the size after each addition:

```python
items.append(2)
sys.getsizeof(items)  # Size remains the same

items.append(3)
sys.getsizeof(items)  # Size still unchanged

items.append(4)
sys.getsizeof(items)  # Size still unchanged

items.append(5)
sys.getsizeof(items)  # Size jumps to a larger value
```

You'll notice that the size doesn't increase with every append operation. Instead, it jumps up periodically, which demonstrates that Python is allocating memory in chunks rather than individually for each new item.

This behavior is by design. Python allocates more memory than needed initially to avoid frequent reallocations as the list grows. Each time the list exceeds its current capacity, Python allocates a larger chunk of memory.

Remember that a list stores references to objects, not the objects themselves. On a 64-bit system, each reference typically requires 8 bytes of memory.
