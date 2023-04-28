# Remove List Elements from the End

## Introduction
In Python, you can remove elements from a list using various methods. One such method is to remove elements from the end of the list. In this challenge, you will write a function that removes `n` elements from the end of a list.

## Problem
Write a function `take_right(lst, n=1)` that takes a list `lst` and an optional integer `n` as arguments and returns a new list with `n` elements removed from the end of the list. If `n` is not provided, the function should remove only the last element from the list.

To solve this problem, you can use slice notation to create a slice of the list with `n` elements taken from the end.

## Example
```py
take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]
```

## Summary
In this challenge, you learned how to remove elements from the end of a list in Python. You also learned how to use slice notation to create a slice of a list with `n` elements taken from the end.