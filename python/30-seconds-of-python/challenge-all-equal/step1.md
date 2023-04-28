# Check if List Elements are Identical

## Problem

Write a function `all_equal(lst)` that takes a list as an argument and returns `True` if all elements in the list are identical, and `False` otherwise.

To solve this problem, you can use the following steps:

1. Use `set()` to eliminate duplicate elements in the list.
2. Use `len()` to check if the length of the set is `1`.
3. If the length of the set is `1`, return `True`. Otherwise, return `False`.

## Example

```python
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```

