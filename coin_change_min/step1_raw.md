# Coin Change Min

Problem: Determine the minimum number of ways to make n cents, given coins of denominations less than n cents.

## Requirements

- Do the coins have to reach exactly n cents?
  - Yes
- Can we assume we have an infinite number of coins to make n cents?
  - Yes
- Do we need to report the combination(s) of coins that represent the minimum?
  - No
- Can we assume the coin denominations are given in sorted order?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- coins: None or n: None -> Exception
- coins: [] or n: 0 -> 0
- coins: [1, 2, 3] or [3, 2, 1] -> 2
