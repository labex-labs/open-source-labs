# List Tail

Write a function `tail(lst)` that takes a list as an argument and returns all elements in the list except for the first one. If the list contains only one element, return the whole list.

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
