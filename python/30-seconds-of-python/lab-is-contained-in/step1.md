# List Containment

## Problem

Write a function `is_contained_in(a, b)` that takes two lists as arguments and returns `True` if all the elements of list `a` are contained in list `b`, regardless of order. Otherwise, the function should return `False`.

To solve this problem, you can use the following approach:

1. Loop through each unique value in list `a`.
2. For each value, check if it appears more times in list `a` than in list `b`.
3. If any value appears more times in list `a` than in list `b`, return `False`.
4. If all values in list `a` appear in list `b` at least as many times as they appear in list `a`, return `True`.

## Example

```python
assert is_contained_in([1, 4], [2, 4, 1]) == True
assert is_contained_in([1, 2, 3], [3, 2, 1]) == True
assert is_contained_in([1, 2, 3], [3, 2, 2, 1]) == False
assert is_contained_in([1, 2, 3], [4, 5, 6]) == False
```
