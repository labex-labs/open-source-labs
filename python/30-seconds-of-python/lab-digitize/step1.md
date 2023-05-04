# Digitize Number

## Problem

Write a function `digitize(n)` that takes a non-negative integer `n` as input and returns a list of its digits. The function should accomplish this by performing the following steps:

1. Convert the input number `n` to a string.
2. Use the `map()` function combined with the `int` function to convert each character in the string to an integer.
3. Return the resulting list of integers.

For example, if the input number is `123`, the function should return the list `[1, 2, 3]`.

## Example

```python
assert digitize(123) == [1, 2, 3]
assert digitize(4567) == [4, 5, 6, 7]
assert digitize(0) == [0]
```
