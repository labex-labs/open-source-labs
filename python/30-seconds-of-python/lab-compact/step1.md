# Compact List

Write a function `compact(lst)` that takes a list as an argument and returns a new list with all falsy values removed. Falsy values include `False`, `None`, `0`, and `""`.

To solve this problem, you can use the `filter()` function to filter out falsy values from the list.

```python
def compact(lst):
  return list(filter(None, lst))
```

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
