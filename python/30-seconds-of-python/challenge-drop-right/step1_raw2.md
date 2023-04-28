# Drop List Elements from the Right

## Introduction

In Python, we can easily remove elements from a list using slice notation. This can be useful when we want to remove a specific number of elements from the right end of a list. In this challenge, you will create a function that takes a list and an optional number of elements to remove from the right end of the list.

## Problem

Write a function `drop_right(a, n = 1)` that takes a list `a` and an optional integer `n` and returns a new list with `n` elements removed from the right end of the list `a`. If `n` is not provided, the function should remove only the last element from the list.

## Example

```py
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```

## Summary

In this challenge, you learned how to remove elements from the right end of a list using slice notation in Python. You also created a function that takes a list and an optional integer and returns a new list with `n` elements removed from the right end of the list.