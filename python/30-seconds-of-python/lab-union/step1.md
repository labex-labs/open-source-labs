# List Union

Write a Python function called `list_union(a, b)` that takes two lists as input and returns a new list containing all the unique elements from both lists. Your function should perform the following steps:

1. Combine the two input lists `a` and `b` into a single list.
2. Remove any duplicates from the combined list.
3. Return the new list containing all the unique elements.

Your function should not modify the input lists `a` and `b`.

```python
def union(a, b):
  return list(set(a + b))
```

```python
union([1, 2, 3], [4, 3, 2]) # [1, 2, 3, 4]
```
