# Math Ops

## Problem

Create a Python class with an insert method that can insert an integer to a list. The class should also support calculating the maximum, minimum, mean, and mode of the list in O(1) time complexity. The class should handle the following scenarios:

- If the input is not valid, it should raise a TypeError.
- If the list is empty, it should raise a ValueError.
- If there are multiple modes, it can return any of the modes.

## Requirements

To achieve the above problem, we need to follow these requirements:

- The inputs may not be valid, so we cannot assume that the inputs are valid.
- The range of inputs is between 0 and 100 inclusive.
- The mean should return a float.
- The other results should return an integer.
- If there are multiple modes, the class can return any of the modes.
- We can assume that the list fits into memory.

## Example Usage

Here are some examples of how to use the class:

- None -> TypeError
- [] -> ValueError
- [5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
  - max: 9
  - min: 2
  - mean: 4.909090909090909
  - mode: 9 or 2
