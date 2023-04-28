# Flatten a List

## Problem

Write a Python function called `flatten(lst)` that takes a list of lists as an argument and returns a flattened list. The function should only flatten the list once, meaning that any nested lists within the original list should be flattened, but any nested lists within those nested lists should remain intact.

To solve this problem, you can use a list comprehension to extract each value from sub-lists in order.

## Example

```py
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```
