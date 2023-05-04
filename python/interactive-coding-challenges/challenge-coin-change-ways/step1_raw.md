# Coin Change Ways

Problem: Counting Ways of Making Change.

- [Explanation](#Explanation)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)
- [Solution Notebook](#Solution-Notebook)

## Explanation

How many ways are there of making change for n, given an array of distinct coins? For example:

Input: n = 4, coins = [1, 2]

Output: 3. 1+1+1+1, 1+2+1, 2+2, would be the ways of making change.

Note that a coin can be used any number of times, and we are counting unique combinations.

## Example Usage

- Input: n = 0, coins = [1, 2] -> Output: 0
- Input: n = 100, coins = [1, 2, 3] -> Output: 884
- Input: n = 1000, coins = [1, 2, 3...99, 100] -> Output: 15658181104580771094597751280645
