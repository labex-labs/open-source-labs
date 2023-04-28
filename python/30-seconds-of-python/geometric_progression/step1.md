# Geometric Progression Challenge

## Problem
Write a function called `geometric_progression` that takes in three parameters:
- `end`: an integer representing the end of the range (inclusive)
- `start`: an optional integer representing the start of the range (inclusive), with a default value of `1`
- `step`: an optional integer representing the common ratio between two terms, with a default value of `2`

The function should return a list containing the numbers in the specified range where the ratio between two terms is `step`. The list should start with `start` and end with `end`. 

If `step` equals `1`, the function should return an error.

You should use `range()`, `math.log()`, and `math.floor()` and a list comprehension to create a list of the appropriate length, applying the step for each element.

## Example
```py
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```

