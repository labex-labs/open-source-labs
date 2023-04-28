# List Intersection Challenge

## Introduction
In Python, you can easily find the common elements between two lists using the set intersection operation. In this challenge, you will be asked to write a function that takes two lists as input and returns a new list containing only the elements that are present in both input lists.

## Problem
Write a function `list_intersection(a, b)` that takes two lists `a` and `b` as input and returns a new list containing only the elements that are present in both `a` and `b`. If there are no common elements, the function should return an empty list.

## Example
```py
list_intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
list_intersection([1, 2, 3], [4, 5, 6]) # []
list_intersection([1, 2, 3], [3, 3, 2]) # [2, 3]
```

## Summary
To solve this challenge, you need to convert the input lists into sets and then use the set intersection operation to find the common elements. Finally, you need to convert the resulting set back into a list and return it.