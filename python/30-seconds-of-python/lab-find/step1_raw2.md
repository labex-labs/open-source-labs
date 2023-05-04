# Find Matching Value

## Introduction

In Python, we can use a list comprehension and `next()` to find the value of the first element in a given list that satisfies a provided testing function. This can be useful in many scenarios, such as finding the first odd number in a list or the first string that starts with a certain letter.

## Problem

Write a function called `find(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments. The function should return the value of the first element in `lst` for which `fn` returns `True`. If no element satisfies the testing function, the function should return `None`.

## Example

```py
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
find(['apple', 'banana', 'cherry'], lambda s: s.startswith('b')) # 'banana'
find([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```

## Summary

In this challenge, you learned how to find the value of the first element in a list that satisfies a provided testing function using a list comprehension and `next()`. This technique can be useful in many scenarios and can help you write more efficient and concise code.
