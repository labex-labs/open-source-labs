# Index of min element

## Introduction

In Python, you can easily find the minimum value in a list using the `min()` function. However, what if you also need to know the index of that minimum value? In this challenge, you will create a function that returns the index of the element with the minimum value in a list.

## Problem

Write a function `min_element_index(arr)` that takes a list of integers `arr` as an argument and returns the index of the element with the minimum value in the list.

To solve this problem, you can use the `min()` function to obtain the minimum value in the list and then use the `list.index()` method to return its index.

## Example

```py
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```

In this example, the minimum value in the list `[3, 5, 2, 6, 10, 7, 9]` is `2`, which is located at index `2`.

## Summary

In this challenge, you learned how to find the index of the element with the minimum value in a list using Python. By using the `min()` function and the `list.index()` method, you can easily obtain the index of the minimum value in a list.