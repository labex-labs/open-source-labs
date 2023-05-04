# Transpose Matrix

## Introduction

In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal. The transpose of a matrix is obtained by exchanging its rows into columns. In Python, we can transpose a two-dimensional list using a simple one-liner code.

## Problem

Write a function called `transpose(lst)` that takes a two-dimensional list as an argument and returns the transpose of the given list.

Follow these steps to solve the problem:

- Use `*lst` to get the provided list as tuples.
- Use `zip()` in combination with `list()` to create the transpose of the given two-dimensional list.

## Example

```py
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
```

## Summary

In this challenge, you learned how to transpose a two-dimensional list using Python. The transpose of a matrix is obtained by exchanging its rows into columns. You can use this technique to manipulate data in a variety of applications, such as data analysis and machine learning.
