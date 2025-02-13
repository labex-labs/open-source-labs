# Transpose Matrix

## Problem

Write a function called `transpose(lst)` that takes a two-dimensional list as an argument and returns the transpose of the given list.

Follow these steps to solve the problem:

- Use `*lst` to get the provided list as tuples.
- Use `zip()` in combination with `list()` to create the transpose of the given two-dimensional list.

## Example

```python
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
```
