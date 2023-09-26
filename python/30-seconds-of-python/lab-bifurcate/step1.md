# Bifurcate List

Write a function `bifurcate(lst, filter)` that takes a list `lst` and a filter `filter` as input and returns a list of two lists. The first list should contain the elements of `lst` that pass the filter, and the second list should contain the elements that do not.

To implement this function, you can use a list comprehension and the `zip()` function. The `zip()` function takes two or more lists as input and returns a list of tuples, where each tuple contains the corresponding elements from each list. For example, `zip([1, 2, 3], [4, 5, 6])` returns `[(1, 4), (2, 5), (3, 6)]`.

You can use this function to iterate over both `lst` and `filter` simultaneously and add the elements to the appropriate list based on whether they pass the filter or not.

```python
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
