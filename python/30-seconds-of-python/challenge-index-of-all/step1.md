# All Indexes of Value

## Problem

Write a Python function called `index_of_all(lst, value)` that takes a list `lst` and a value `value` as arguments and returns a list of indexes of all the occurrences of `value` in `lst`.

To solve this problem, you can use `enumerate()` and a list comprehension to check each element for equality with `value` and adding `i` to the result.

## Example

```py
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
