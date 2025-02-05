# Split list into chunks

Write a function `chunk(lst, size)` that takes a list `lst` and a positive integer `size` as arguments and returns a list of smaller lists, each of which has a maximum size of `size`. If the length of `lst` is not evenly divisible by `size`, the last list in the returned list should contain the remaining elements.

```python
from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
```

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
```
