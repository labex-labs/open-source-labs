# Weighted Average

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

