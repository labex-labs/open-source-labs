# Unique Elements in List

Write a Python function called `unique_elements` that takes a list as input and returns a new list containing only the unique elements. Your function should perform the following steps:

- Create a `set` from the list to discard duplicated values.
- Return a `list` from the set.

Your function should have the following signature:

```python
def unique_elements(li: List) -> List:
```

```py
def unique_elements(li):
  return list(set(li))
```

```py
unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]
```
