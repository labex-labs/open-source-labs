# Find the Last Matching Value

## Introduction

In Python, we can use list comprehension and `next()` to find the value of the last element in a list that satisfies a given testing function. This challenge will test your ability to use these tools to solve a problem.

## Problem

Write a function `find_last(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments. The function should return the value of the last element in `lst` for which `fn` returns `True`. If no element satisfies the testing function, the function should return `None`.

To solve this problem, you should use a list comprehension and `next()` to iterate through the list in reverse order and return the last element that satisfies the testing function.

## Example

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
find_last([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```

In the first example, the function should return `3` because it is the last odd number in the list. In the second example, the function should return `None` because there are no odd numbers in the list.

## Summary

In this challenge, you learned how to use list comprehension and `next()` to find the value of the last element in a list that satisfies a given testing function. This is a useful tool for filtering and processing data in Python.
