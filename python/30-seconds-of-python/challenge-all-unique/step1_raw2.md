# Title

Check for Duplicates in a List

## Introduction

In Python, a list is a collection of items that are ordered and changeable. Sometimes, we need to check if a list has any duplicate elements. In this challenge, you will write a Python function to check if a list has any duplicates.

## Problem

Write a Python function called `has_duplicates(lst)` that takes a list as an argument and returns `True` if the list has any duplicate elements, otherwise returns `False`.

To solve this problem, you can follow these steps:

1. Convert the list to a set to remove duplicates.
2. Compare the length of the set with the length of the original list.
3. If the lengths are equal, then the list has no duplicates, otherwise it has duplicates.

## Example

```python
has_duplicates([1, 2, 3, 4, 5]) # False
has_duplicates([1, 2, 3, 4, 5, 5]) # True
has_duplicates(['apple', 'banana', 'orange', 'banana']) # True
has_duplicates([]) # False
```

## Summary

In this challenge, you learned how to check for duplicates in a list using Python. You can use this function to ensure that your lists only contain unique elements.
