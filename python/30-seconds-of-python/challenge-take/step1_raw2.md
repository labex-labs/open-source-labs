# Remove List Elements

## Introduction
In Python, we can easily remove elements from a list using slice notation. Slice notation allows us to create a new list by taking a portion of an existing list. In this challenge, you will be asked to write a function that removes a specified number of elements from the beginning of a list.

## Problem

Write a function `take(itr, n=1)` that takes a list `itr` and an integer `n` as arguments and returns a new list with `n` elements removed from the beginning of the list. If `n` is greater than the length of the list, return the original list.

## Example

```py
take([1, 2, 3], 1) # [2, 3]
take([1, 2, 3], 2) # [3]
take([1, 2, 3], 3) # []
take([1, 2, 3], 4) # []
```

## Summary
In this challenge, you learned how to remove elements from the beginning of a list using slice notation in Python. You also wrote a function that takes a list and an integer as arguments and returns a new list with a specified number of elements removed from the beginning.