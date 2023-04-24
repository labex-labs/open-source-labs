# Coin Change Ways

## Problem

Given an integer n and an array of distinct coins, write a function to count the number of ways of making change for n using the coins in the array. A coin can be used any number of times, and we are counting unique combinations.

For example, if n = 4 and coins = [1, 2], there are 3 ways of making change: 1+1+1+1, 1+2+1, and 2+2.

## Requirements

To solve this problem, you will need to:

- Write a function that takes two arguments: an integer n and an array of distinct coins.
- Use dynamic programming to count the number of ways of making change for n using the coins in the array.
- Return the number of unique combinations.

## Example

Input: n = 4, coins = [1, 2]

Output: 3. 1+1+1+1, 1+2+1, 2+2, would be the ways of making change.
