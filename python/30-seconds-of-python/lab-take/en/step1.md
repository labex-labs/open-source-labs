# Remove List Elements

Write a function `take(itr, n=1)` that takes a list `itr` and an integer `n` as arguments and returns a new list with `n` elements removed from the beginning of the list. If `n` is greater than the length of the list, return the original list.

```python
def take(itr, n = 1):
  return itr[:n]
```

```python
take([1, 2, 3], 5) # [1, 2, 3]
take([1, 2, 3], 0) # []
```
