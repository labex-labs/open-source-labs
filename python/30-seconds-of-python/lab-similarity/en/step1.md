# List Similarity

Write a function `similarity(a, b)` that takes two lists `a` and `b` as arguments and returns a new list that contains only the elements that exist in both `a` and `b`.

To solve this problem, we can use list comprehension to iterate over the elements of `a` and check if they exist in `b`. If an element exists in both lists, we add it to a new list.

```python
def similarity(a, b):
  return [item for item in a if item in b]
```

```python
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```
