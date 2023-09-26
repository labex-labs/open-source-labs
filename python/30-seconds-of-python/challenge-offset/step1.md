# Offset List Elements

## Problem

Write a function `offset(lst, offset)` that takes a list `lst` and an integer `offset` as arguments and returns a new list with the specified amount of elements moved to the end of the list. If the `offset` is positive, move the first `offset` elements to the end of the list. If the `offset` is negative, move the last `offset` elements to the beginning of the list.

## Example

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
