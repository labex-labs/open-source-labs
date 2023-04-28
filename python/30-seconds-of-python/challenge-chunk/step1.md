# Split list into chunks

## Problem

Write a function `chunk(lst, size)` that takes a list `lst` and a positive integer `size` as arguments and returns a list of smaller lists, each of which has a maximum size of `size`. If the length of `lst` is not evenly divisible by `size`, the last list in the returned list should contain the remaining elements.

## Example

```py
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5], 3) # [[1, 2, 3], [4, 5]]
chunk([1, 2, 3, 4, 5], 1) # [[1], [2], [3], [4], [5]]
```
