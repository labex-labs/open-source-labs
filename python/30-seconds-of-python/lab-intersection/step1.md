# List Intersection Challenge

Write a function `list_intersection(a, b)` that takes two lists `a` and `b` as input and returns a new list containing only the elements that are present in both `a` and `b`. If there are no common elements, the function should return an empty list.

```py
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```py
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
