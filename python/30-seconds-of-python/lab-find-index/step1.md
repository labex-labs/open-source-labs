# Find Matching Index

Write a function `find_index(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments. The function should return the index of the first element in `lst` for which `fn` returns `True`.

```py
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
```

```py
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
