# Check if Two Lists Have the Same Contents

## Introduction

In programming, it is often necessary to check if two lists contain the same elements, regardless of their order. This can be useful in a variety of situations, such as checking if two sets of data have the same values or verifying if a function is returning the expected output. In this challenge, you will write a function that checks if two lists have the same contents.

## Problem

Write a function `have_same_contents(a, b)` that takes two lists as arguments and returns `True` if they have the same contents, `False` otherwise. The function should check if the two lists contain the same elements, regardless of their order.

To solve this problem, you can follow these steps:

1. Use `set()` on the combination of both lists to find the unique values.
2. Iterate over them with a `for` loop comparing the `count()` of each unique value in each list.
3. Return `False` if the counts do not match for any element, `True` otherwise.

## Example

```py
have_same_contents([1, 2, 4], [2, 4, 1]) # True
have_same_contents([1, 2, 4], [2, 4, 5]) # False
```

## Summary

In this challenge, you have learned how to check if two lists have the same contents, regardless of their order. By using the `set()` function and iterating over the unique values, you can compare the `count()` of each element in both lists to determine if they have the same contents.
