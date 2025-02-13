# Find Parity Outliers

## Problem

Write a function `find_parity_outliers(nums)` that takes a list of integers `nums` as an argument and returns a list of all the parity outliers in `nums`.

To solve this problem, you can follow these steps:

1. Use `collections.Counter` with a list comprehension to count even and odd values in the list.
2. Use `collections.Counter.most_common()` to get the most common parity.
3. Use a list comprehension to find all elements that do not match the most common parity.

## Example

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```

In the example above, the majority of the elements in the list are even, so the parity outliers are the odd elements 1 and 3.
