# List Difference Based on Function

## Introduction
In Python, we can easily find the difference between two lists using the built-in `set()` function. However, what if we want to find the difference based on a specific function applied to each element in both lists? In this challenge, you will create a function that takes in two lists and a function, and returns the difference between the two lists after applying the provided function to each list element of both.

## Problem
Create a function called `difference_by(a, b, fn)` that takes in three parameters:
- `a`: a list of elements
- `b`: a list of elements
- `fn`: a function that will be applied to each element in both lists

The function should return a list of elements that are in list `a` but not in list `b`, after applying the provided function `fn` to each element in both lists.

To solve this problem, you can follow these steps:
1. Create a `set`, using `map()` to apply `fn` to each element in `b`.
2. Use a list comprehension in combination with `fn` on `a` to only keep values not contained in the previously created set, `_b`.

## Example
```py
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```

## Summary
In this challenge, you have learned how to find the difference between two lists based on a specific function applied to each element in both lists. You have also practiced using `map()`, `set()`, and list comprehension to solve the problem.