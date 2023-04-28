# Split list into chunks

## Introduction
In Python, we often need to split a list into smaller lists of a specified size. This can be useful for various purposes, such as processing data in batches or displaying data in a paginated format. In this challenge, you will be tasked with writing a function that can split a list into smaller lists of a specified size.

## Problem
Write a function `chunk(lst, size)` that takes a list `lst` and a positive integer `size` as arguments and returns a list of smaller lists, each of which has a maximum size of `size`. If the length of `lst` is not evenly divisible by `size`, the last list in the returned list should contain the remaining elements.

## Example
```py
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5], 3) # [[1, 2, 3], [4, 5]]
chunk([1, 2, 3, 4, 5], 1) # [[1], [2], [3], [4], [5]]
```

## Summary
In this challenge, you have learned how to split a list into smaller lists of a specified size. You have written a function that takes a list and a positive integer as arguments and returns a list of smaller lists, each of which has a maximum size of the given integer. This can be useful for various purposes, such as processing data in batches or displaying data in a paginated format.