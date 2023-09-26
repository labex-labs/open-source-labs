# Partial Sum List

## Problem

Write a function `partial_sum(lst)` that takes a list of numbers as an argument and returns a list of partial sums. Your function should perform the following steps:

1. Use `itertools.accumulate()` to create the accumulated sum for each element in the list.
2. Use `list()` to convert the result into a list.
3. Return the list of partial sums.

## Example

```python
partial_sum([1, 2, 3, 4, 5]) # [1, 3, 6, 10, 15]
partial_sum([2, 4, 6, 8, 10]) # [2, 6, 12, 20, 30]
partial_sum([5, 10, 15, 20, 25]) # [5, 15, 30, 50, 75]
```
