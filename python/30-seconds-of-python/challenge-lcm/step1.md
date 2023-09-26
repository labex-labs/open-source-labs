# Least Common Multiple Challenge

## Problem

Write a function `lcm(numbers)` that takes a list of numbers as an argument and returns their least common multiple. Your function should use the following formula to calculate the LCM of two numbers `x` and `y`: `lcm(x, y) = x * y / gcd(x, y)`, where `gcd(x, y)` is the greatest common divisor of `x` and `y`.

To solve this problem, you can use the `functools.reduce()` function to apply the `lcm()` formula to all the numbers in the list. You can also use the `math.gcd()` function to calculate the greatest common divisor of two numbers.

## Example

```python
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```
