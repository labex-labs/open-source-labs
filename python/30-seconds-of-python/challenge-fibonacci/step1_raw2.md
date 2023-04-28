# Fibonacci Challenge

## Introduction
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. It starts with 0 and 1, and the next number is the sum of the previous two numbers. In this challenge, you will write a function that generates a list containing the Fibonacci sequence up until the nth term.

## Problem
Write a function called `fibonacci(n)` that takes an integer `n` as its parameter and returns a list containing the Fibonacci sequence up until the nth term. 

To solve this problem, you can follow these steps:
1. Create an empty list called `sequence`.
2. If `n` is less than or equal to 0, append 0 to the `sequence` list and return the list.
3. Append 0 and 1 to the `sequence` list.
4. Use a while loop to add the sum of the last two numbers of the `sequence` list to the end of the list, until the length of the list reaches `n`.
5. Return the `sequence` list.

## Example
```py
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```

## Summary
In this challenge, you have learned how to generate a list containing the Fibonacci sequence up until the nth term. You have also learned how to use a while loop to add the sum of the last two numbers of a list to the end of the list.