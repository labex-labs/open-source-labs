# List Initial

## Introduction
In Python, a list is a collection of items that are ordered and changeable. Sometimes, we need to remove the last element of a list and get all the other elements. In this challenge, you need to create a function that returns all the elements of a list except the last one.

## Problem
Write a Python function called `initial(lst)` that takes a list as an argument and returns all the elements of the list except the last one.

### Example
```py
initial([1, 2, 3]) # [1, 2]
initial(['apple', 'banana', 'orange', 'grape']) # ['apple', 'banana', 'orange']
```

## Summary
To solve this challenge, you need to use Python's list slicing feature. The `lst[:-1]` syntax returns all but the last element of the list.