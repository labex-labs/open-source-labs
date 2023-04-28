# Deep Flatten List

## Introduction

In Python, a list can contain other lists as elements, and those lists can contain even more lists as elements, forming a nested structure. The process of flattening a nested list means to convert it into a one-dimensional list, where all the elements are at the same level. In this challenge, you will be asked to write a function that deep flattens a list, meaning that it will flatten all the nested lists recursively.

## Problem

Write a function `deep_flatten(lst)` that takes a list `lst` as an argument and returns a new list that is the deep flattened version of `lst`. The function should use recursion and the `isinstance()` function with `collections.abc.Iterable` to check if an element is iterable. If an element is iterable, the function should apply `deep_flatten()` recursively to that element. Otherwise, the function should return a list containing only that element.

## Example

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
deep_flatten([1, [2, [3, [4]]]]) # [1, 2, 3, 4]
deep_flatten([1, 2, 3, 4]) # [1, 2, 3, 4]
deep_flatten([]) # []
```

## Summary

In this challenge, you have learned how to deep flatten a list using recursion and the `isinstance()` function with `collections.abc.Iterable`. This technique can be useful when dealing with nested data structures, such as lists of lists.