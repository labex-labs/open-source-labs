# Fibonacci Challenge

## Problem

Write a function called `fibonacci(n)` that takes an integer `n` as its parameter and returns a list containing the Fibonacci sequence up until the nth term.

To solve this problem, you can follow these steps:

1. Create an empty list called `sequence`.
2. If `n` is less than or equal to 0, append 0 to the `sequence` list and return the list.
3. Append 0 and 1 to the `sequence` list.
4. Use a while loop to add the sum of the last two numbers of the `sequence` list to the end of the list, until the length of the list reaches `n`.
5. Return the `sequence` list.

## Example

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
