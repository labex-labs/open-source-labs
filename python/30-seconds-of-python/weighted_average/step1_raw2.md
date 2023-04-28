# Weighted Average

## Introduction
A weighted average is a type of average that takes into account the importance, or weight, of each value in a set of numbers. In this challenge, you will create a function that calculates the weighted average of a list of numbers.

## Problem
Write a function `weighted_average(nums, weights)` that takes in two lists of equal length: `nums` and `weights`. The function should return the weighted average of the numbers in `nums`, where each number is multiplied by its corresponding weight in `weights`. The weighted average is calculated by dividing the sum of the products of each number and its weight by the sum of the weights.

## Example
```py
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```

Explanation:
```
(1 * 0.6 + 2 * 0.2 + 3 * 0.3) / (0.6 + 0.2 + 0.3) = 1.72727
```

## Summary
In this challenge, you learned how to calculate the weighted average of a list of numbers using Python. You used the `sum()` function to sum the products of the numbers by their weight and to sum the weights. You also used the `zip()` function and a list comprehension to iterate over the pairs of values and weights.