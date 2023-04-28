# Least Common Multiple Challenge

## Introduction
In mathematics, the least common multiple (LCM) is the smallest positive integer that is divisible by two or more numbers without leaving any remainder. For example, the LCM of 4 and 6 is 12, because 12 is the smallest number that is divisible by both 4 and 6.

## Problem
Write a function `lcm(numbers)` that takes a list of numbers as an argument and returns their least common multiple. Your function should use the following formula to calculate the LCM of two numbers `x` and `y`: `lcm(x, y) = x * y / gcd(x, y)`, where `gcd(x, y)` is the greatest common divisor of `x` and `y`.

To solve this problem, you can use the `functools.reduce()` function to apply the `lcm()` formula to all the numbers in the list. You can also use the `math.gcd()` function to calculate the greatest common divisor of two numbers.

## Example
```py
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```

## Summary
In this challenge, you have learned how to calculate the least common multiple of a list of numbers using the `functools.reduce()` and `math.gcd()` functions. The `lcm()` function uses the `lcm(x, y) = x * y / gcd(x, y)` formula to calculate the LCM of two numbers.