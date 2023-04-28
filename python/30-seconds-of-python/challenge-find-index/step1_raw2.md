# Find Matching Index

## Introduction

In Python, it is often necessary to find the index of the first element in a list that satisfies a certain condition. This can be achieved using a list comprehension, `enumerate()`, and `next()`. In this challenge, you will be tasked with writing a function that finds the index of the first element in a list that satisfies a given testing function.

## Problem

Write a function `find_index(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments. The function should return the index of the first element in `lst` for which `fn` returns `True`.

## Example

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```

## Summary

In this challenge, you have learned how to find the index of the first element in a list that satisfies a given testing function. This can be achieved using a list comprehension, `enumerate()`, and `next()`.
