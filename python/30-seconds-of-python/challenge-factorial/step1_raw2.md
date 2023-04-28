# Factorial

## Introduction
In mathematics, the factorial of a non-negative integer `n`, denoted by `n!`, is the product of all positive integers less than or equal to `n`. For example, `5! = 5 x 4 x 3 x 2 x 1 = 120`. In this challenge, you will write a Python function to calculate the factorial of a given number using recursion.

## Problem
Write a function `factorial(num)` that takes a non-negative integer `num` as an argument and returns its factorial. The function should use recursion to calculate the factorial. If `num` is less than or equal to `1`, return `1`. Otherwise, return the product of `num` and the factorial of `num - 1`. The function should throw an exception if `num` is a negative or a floating-point number.

## Example
```py
factorial(6) # 720
```

## Summary
In this challenge, you learned how to calculate the factorial of a number using recursion. You also learned how to handle exceptions in Python.