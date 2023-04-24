# Coin Change

## Problem

Given a set of coins of different denominations and a total amount of money n, determine the total number of unique ways to make change for n cents. The coins provided have denominations less than n cents.

## Requirements

To solve this problem, the following requirements must be met:

- The coins must reach exactly n cents.
- An infinite number of coins can be assumed to make n cents.
- The combination(s) of coins that represent the minimum do not need to be reported.
- The coin denominations are not given in sorted order.
- The solution must fit in memory.

## Example Usage

The following examples demonstrate the usage of the coin change problem:

- coins: None or n: None -> Exception
- coins: [] or n: 0 -> 0
- coins: [1, 2, 3], n: 5 -> 5
