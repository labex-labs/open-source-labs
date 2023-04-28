# N Minimum Elements

## Problem

Write a function called `min_n(lst, n = 1)` that takes in a list `lst` and an optional integer `n` (default value of `1`). The function should return a new list containing the `n` smallest elements from the original list `lst`. If `n` is not provided, the function should return a list containing the smallest element from `lst`.

If `n` is greater than or equal to the length of `lst`, the function should return the original list sorted in ascending order.

Your function should accomplish this by following these steps:

1. Use the built-in `sorted()` function to sort the list in ascending order.
2. Use slice notation to get the specified number of elements.
3. Return the resulting list.

## Example

```py
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
```
