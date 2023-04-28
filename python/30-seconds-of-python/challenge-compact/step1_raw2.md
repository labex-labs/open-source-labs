# Compact List

## Introduction

In this challenge, you need to write a Python function that removes falsy values from a list.

## Problem

Write a function `compact(lst)` that takes a list as an argument and returns a new list with all falsy values removed. Falsy values include `False`, `None`, `0`, and `""`.

To solve this problem, you can use the `filter()` function to filter out falsy values from the list.

## Example

```py
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```

## Summary

In this challenge, you have learned how to remove falsy values from a list using the `filter()` function in Python.
