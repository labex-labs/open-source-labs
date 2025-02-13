# Check for Duplicates in a List

## Problem

Write a Python function called `has_duplicates(lst)` that takes a list as an argument and returns `True` if the list contains any duplicates, and `False` otherwise.

To solve this problem, you can use the following steps:

1. Use the `set()` function to remove duplicates from the list.
2. Compare the length of the original list with the length of the set. If they are the same, then there are no duplicates. If they are different, then there are duplicates.

## Example

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
print(has_duplicates(x)) # True
print(has_duplicates(y)) # False
```
