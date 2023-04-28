# Hamming Distance Challenge

## Introduction
The Hamming distance is a measure of the difference between two strings of equal length. In other words, it is the number of positions at which the corresponding symbols are different. In this challenge, you will be asked to write a function that calculates the Hamming distance between two values.

## Problem
Write a function `hamming_distance(a, b)` that takes two integers as arguments and returns the Hamming distance between them. The function should perform the following steps:

1. Use the XOR operator (`^`) to find the bit difference between the two numbers.
2. Use `bin()` to convert the result to a binary string.
3. Convert the string to a list and use `count()` of `str` class to count and return the number of `1`s in it.

## Example
```py
hamming_distance(2, 3) # 1
hamming_distance(10, 4) # 2
hamming_distance(0, 255) # 8
```

## Summary
In this challenge, you have learned how to calculate the Hamming distance between two values using Python. The Hamming distance is a useful measure of the difference between two strings of equal length, and it has many applications in computer science and information theory.