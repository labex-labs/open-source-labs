# Initialize List with Values

## Introduction

In Python, a list is a collection of items that are ordered and changeable. Sometimes, we need to initialize a list with a specific value or set of values. In this challenge, you will create a function that initializes and fills a list with the specified value.

## Problem

Write a function `initialize_list_with_values(n, val=0)` that takes in two parameters:

- `n` (integer) representing the length of the list to be created.
- `val` (integer) representing the value to be used to fill the list. If `val` is not provided, the default value of `0` should be used.

The function should return a list of length `n` filled with the specified value.

## Example

```py
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
initialize_list_with_values(3) # [0, 0, 0]
```

## Summary

In this challenge, you learned how to initialize and fill a list with a specified value using a list comprehension and the `range()` function. You also learned how to set a default value for a function parameter.
