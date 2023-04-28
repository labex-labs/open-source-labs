# Offset List Elements

## Introduction
In Python, lists are a commonly used data structure. Sometimes, you may need to move certain elements of a list to the end of the list. In this challenge, you will write a function that takes a list and an offset as arguments and returns a new list with the specified amount of elements moved to the end of the list.

## Problem
Write a function `offset(lst, offset)` that takes a list `lst` and an integer `offset` as arguments and returns a new list with the specified amount of elements moved to the end of the list. If the `offset` is positive, move the first `offset` elements to the end of the list. If the `offset` is negative, move the last `offset` elements to the beginning of the list.

## Example
```py
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```

## Summary
In this challenge, you wrote a function that takes a list and an offset as arguments and returns a new list with the specified amount of elements moved to the end of the list. You used slice notation to get the two slices of the list and combine them before returning.