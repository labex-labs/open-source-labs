# List Similarity

## Introduction

In Python, it is often necessary to compare two lists and find the elements that exist in both lists. This can be achieved by using list comprehension, a powerful feature of Python that allows us to create new lists based on existing lists.

## Problem

Write a function `similarity(a, b)` that takes two lists `a` and `b` as arguments and returns a new list that contains only the elements that exist in both `a` and `b`.

To solve this problem, we can use list comprehension to iterate over the elements of `a` and check if they exist in `b`. If an element exists in both lists, we add it to a new list.

## Example

```py
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```

In this example, the function `similarity` takes two lists `[1, 2, 3]` and `[1, 2, 4]` as arguments. The function returns a new list `[1, 2]` that contains only the elements that exist in both lists.

## Summary

In this challenge, you have learned how to find the similarity between two lists using list comprehension in Python. This is a useful technique that can be used in many different applications, such as data analysis and machine learning.
