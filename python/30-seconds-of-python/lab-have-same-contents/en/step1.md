# Check if Two Lists Have the Same Contents

Write a function `have_same_contents(a, b)` that takes two lists as arguments and returns `True` if they have the same contents, `False` otherwise. The function should check if the two lists contain the same elements, regardless of their order.

To solve this problem, you can follow these steps:

1. Use `set()` on the combination of both lists to find the unique values.
2. Iterate over them with a `for` loop comparing the `count()` of each unique value in each list.
3. Return `False` if the counts do not match for any element, `True` otherwise.

```python
def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v) != b.count(v):
      return False
  return True
```

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
```
