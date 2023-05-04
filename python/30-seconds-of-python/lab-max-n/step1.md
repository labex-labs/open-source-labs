# N Max Elements

Write a function `max_n(lst, n = 1)` that takes a list `lst` and an optional integer `n` as arguments and returns a list of the `n` maximum elements from the provided list. If `n` is not provided, the function should return a list containing the maximum element of the list. If `n` is greater than or equal to the length of the list, the function should return the original list sorted in descending order.

Your task is to implement the `max_n()` function.

```py
def max_n(lst, n = 1):
  return sorted(lst, reverse = True)[:n]
```

```py
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
```
