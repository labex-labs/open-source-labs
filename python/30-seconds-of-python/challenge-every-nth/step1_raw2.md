# Every nth element in list

## Introduction

In Python, we can access elements in a list using their index. Sometimes we may want to extract every `nth` element from a list. In this challenge, you are tasked with writing a function that takes a list and an integer `nth` as arguments and returns a new list containing every `nth` element of the original list.

## Problem

Write a function `every_nth(lst, nth)` that takes a list `lst` and an integer `nth` as arguments and returns a new list containing every `nth` element of the original list.

### Example

```py
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```

### Constraints

- The input list `lst` will contain at least `nth` elements.
- The value of `nth` will be greater than 0.

## Summary

In this challenge, you learned how to extract every `nth` element from a list in Python. You can achieve this by using slice notation to create a new list that contains every `nth` element of the given list.
