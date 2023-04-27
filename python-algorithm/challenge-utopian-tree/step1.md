# Utopian Tree

## Problem

The Utopian Tree problem involves calculating the height of a tree after a certain number of growth cycles. The tree starts at a height of 1 meter and doubles in height during the spring growth cycle. During the summer growth cycle, the tree grows by 1 meter. The growth cycles alternate between spring and summer, with the first cycle being spring. The problem requires the programmer to write a function that takes the number of growth cycles as input and returns the height of the tree after those cycles.

For example, if the input is 3, the function should return 6. This is because the tree starts at a height of 1 meter, doubles to 2 meters during the first spring cycle, grows by 1 meter to 3 meters during the first summer cycle, doubles to 6 meters during the second spring cycle, and grows by 1 meter to 7 meters during the second summer cycle.

## Requirements

To solve the Utopian Tree problem, the programmer must write a function that takes an integer as input and returns an integer as output. The function should calculate the height of the tree after the specified number of growth cycles, using the rules described in the problem statement.

## Example Usage

```python
def utopianTree(n):
    height = 1
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    return height

print(utopianTree(3)) # Output: 6
```
