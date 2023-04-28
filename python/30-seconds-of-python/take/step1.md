# Remove List Elements

## Problem

Write a function `take(itr, n=1)` that takes a list `itr` and an integer `n` as arguments and returns a new list with `n` elements removed from the beginning of the list. If `n` is greater than the length of the list, return the original list.

## Example

```py
take([1, 2, 3], 1) # [2, 3]
take([1, 2, 3], 2) # [3]
take([1, 2, 3], 3) # []
take([1, 2, 3], 4) # []
```

