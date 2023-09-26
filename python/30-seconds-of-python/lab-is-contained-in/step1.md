# List Containment

Write a function `is_contained_in(a, b)` that takes two lists as arguments and returns `True` if all the elements of list `a` are contained in list `b`, regardless of order. Otherwise, the function should return `False`.

To solve this problem, you can use the following approach:

1. Loop through each unique value in list `a`.
2. For each value, check if it appears more times in list `a` than in list `b`.
3. If any value appears more times in list `a` than in list `b`, return `False`.
4. If all values in list `a` appear in list `b` at least as many times as they appear in list `a`, return `True`.

```python
def is_contained_in(a, b):
  for v in set(a):
    if a.count(v) > b.count(v):
      return False
  return True
```

```python
is_contained_in([1, 4], [2, 4, 1]) # True
```
