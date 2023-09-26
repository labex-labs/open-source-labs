# Drop List Elements from the Right

Write a function `drop_right(a, n = 1)` that takes a list `a` and an optional integer `n` and returns a new list with `n` elements removed from the right end of the list `a`. If `n` is not provided, the function should remove only the last element from the list.

```python
def drop_right(a, n = 1):
  return a[:-n]
```

```python
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```
