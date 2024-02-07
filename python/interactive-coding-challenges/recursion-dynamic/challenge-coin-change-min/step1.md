# Coin Change Min

## Problem

Given a set of coins with denominations less than n cents, we need to determine the minimum number of ways to make n cents using these coins. The coins can be used in any combination and we have an infinite number of coins of each denomination. We do not need to report the combination(s) of coins that represent the minimum.

## Requirements

To solve this problem, we need to consider the following requirements:

- The coins have to reach exactly n cents.
- We can assume we have an infinite number of coins to make n cents.
- We do not need to report the combination(s) of coins that represent the minimum.
- We cannot assume the coin denominations are given in sorted order.
- We can assume this fits memory.

## Example Usage

Here are some examples of how this function can be used:

- coins: None or n: None -> Exception
- coins: [] or n: 0 -> 0
- coins: [1, 2, 3] or [3, 2, 1] -> 2
