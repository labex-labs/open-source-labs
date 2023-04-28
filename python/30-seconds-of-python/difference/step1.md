# List Difference

## Problem
Write a Python function called `list_difference(a, b)` that takes two lists as arguments and returns the difference between them. The function should not filter out duplicate values. To solve this problem, you can follow these steps:
1. Create a set from the second list `b`.
2. Use a list comprehension on the first list `a` to only keep values not contained in the previously created set `_b`.
3. Return the resulting list.

## Example
```py
list_difference([1, 2, 3], [1, 2, 4]) # [3]
```

