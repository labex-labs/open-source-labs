# Hamming Distance Challenge

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

