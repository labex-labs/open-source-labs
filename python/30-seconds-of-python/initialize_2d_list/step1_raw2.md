# Initialize 2D List

## Introduction

In Python, a 2D list is a list of lists. It is a useful data structure for representing grids, tables, and matrices. Initializing a 2D list involves creating a list of lists with a given width and height and initializing each element with a default value.

## Problem

Write a function `initialize_2d_list(w, h, val=None)` that initializes a 2D list of given width and height and value. The function should return a list of `h` rows where each row is a list with length `w`, initialized with `val`. If `val` is not provided, the default value should be `None`.

## Example

```py
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
initialize_2d_list(3, 3, "x") # [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
initialize_2d_list(2, 3) # [[None, None], [None, None], [None, None]]
```

## Summary

In this challenge, you learned how to initialize a 2D list in Python. You used a list comprehension and `range()` to generate `h` rows where each is a list with length `w`, initialized with a default value. You also learned how to set the default value to `None` if no value is provided.