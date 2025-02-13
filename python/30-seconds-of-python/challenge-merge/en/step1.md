# Merge Lists

## Problem

Write a function called `merge(*args, fill_value=None)` that takes in two or more lists as arguments and returns a list of lists. The function should combine elements from each of the input lists based on their positions. If a list is shorter than the longest list, the function should use `fill_value` for the remaining items. If `fill_value` is not provided, it should default to `None`.

Your task is to implement the `merge()` function.

## Example

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
