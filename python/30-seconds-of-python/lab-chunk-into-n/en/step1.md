# Split List into N Chunks

Write a Python function called `chunk_into_n(lst, n)` that takes a list `lst` and an integer `n` as input and returns a list of `n` smaller lists, each containing an equal number of elements from the original list. If the original list cannot be split evenly into `n` smaller lists, the final chunk should contain the remaining elements.

To solve this problem, you can follow these steps:

1. Calculate the size of each chunk by dividing the length of the original list by `n` and rounding up to the nearest integer using the `math.ceil()` function.
2. Create a new list of size `n` using the `list()` and `range()` functions.
3. Use the `map()` function to map each element of the new list to a chunk of the original list the length of `size`.
4. Return the list of smaller lists.

Your function should have the following signature:

```python
def chunk_into_n(lst: list, n: int) -> list:
```

```python
from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
```

```python
chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) # [[1, 2], [3, 4], [5, 6], [7]]
```
