# List Intersection Based on Function

## Introduction

In Python, we can find the intersection of two lists using the `set()` and `intersection()` methods. However, what if we want to find the intersection based on a specific function applied to each element in both lists? In this challenge, you will create a function that takes in two lists and a function, and returns a list of elements that exist in both lists, after applying the provided function to each list element of both.

## Problem

Write a function `intersection_by(a, b, fn)` that takes in two lists `a` and `b`, and a function `fn`. The function should return a list of elements that exist in both lists, after applying the provided function to each list element of both.

### Input

- Two lists `a` and `b` (1 <= len(a), len(b) <= 1000)
- A function `fn` that takes in one argument and returns a value

### Output

- A list of elements that exist in both lists, after applying the provided function to each list element of both.

### Example

```py
intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```

### Note

In the example above, the function `floor()` is applied to each element in both lists. The resulting sets are `{2, 3}` and `{2, 1}`. The intersection of these sets is `{2}`, which is then returned as a list.

## Summary

In this challenge, you have learned how to find the intersection of two lists based on a specific function applied to each element in both. You have written a function `intersection_by(a, b, fn)` that takes in two lists and a function, and returns a list of elements that exist in both lists, after applying the provided function to each list element of both.
