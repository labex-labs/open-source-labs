# Rotate List Elements

## Problem

Write a function `roll(lst, offset)` that takes in a list `lst` and an integer `offset`. The function should move the specified amount of elements to the start of the list. If `offset` is positive, the elements should be moved from the end of the list to the start. If `offset` is negative, the elements should be moved from the start of the list to the end.

Return the modified list.

## Example

```py
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
```
