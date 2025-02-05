# Drop List Elements from the Left

Write a function `drop(a, n=1)` that takes a list `a` and an optional integer `n` as arguments and returns a new list with `n` elements removed from the left of the original list. If `n` is not provided, the function should remove only the first element of the list.

```python
def drop(a, n = 1):
  return a[n:]
```

```python
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```
