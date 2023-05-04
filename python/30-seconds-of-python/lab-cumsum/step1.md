# Partial Sum List

Write a function `partial_sum(lst)` that takes a list of numbers as an argument and returns a list of partial sums. Your function should perform the following steps:

1. Use `itertools.accumulate()` to create the accumulated sum for each element in the list.
2. Use `list()` to convert the result into a list.
3. Return the list of partial sums.

```py
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```py
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```
