# Find the Last Matching Index

Write a function `find_last_index(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should return the index of the last element in `lst` for which `fn` returns `True`. If no element satisfies the condition, the function should return `-1`.

```python
def find_last_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
```
