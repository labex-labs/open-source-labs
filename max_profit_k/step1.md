# Max Profit K

## Problem

Given a list of stock prices on each consecutive day, determine the max profits with k transactions. The problem requires the determination of the maximum profit that can be obtained from a list of stock prices on consecutive days, considering k transactions. The transactions consist of buying and selling stocks, and the maximum number of transactions is limited to k. The solution should return the maximum profit and the days to buy and sell.

## Requirements

The following requirements must be met to solve the problem:

- k represents the number of sell transactions.
- The prices input is an array of integers.
- The inputs may not be valid.
- If the prices are all decreasing and there is no opportunity to make a profit, the solution should return 0.
- The output should be the maximum profit and days to buy and sell.
- The solution should fit memory.

## Example Usage

The following examples illustrate the usage of the solution:

- Prices: None or k: None -> None
- Prices: [] or k <= 0 -> []
- Prices: [0, -1, -2, -3, -4, -5]
  - (max profit, list of transactions)
  - (0, [])
- Prices: [2, 5, 7, 1, 4, 3, 1, 3] k: 3
  - (max profit, list of transactions)
  - (10, [Type.SELL day: 7 price: 3,
    Type.BUY day: 6 price: 1,
    Type.SELL day: 4 price: 4,
    Type.BUY day: 3 price: 1,
    Type.SELL day: 2 price: 7,
    Type.BUY day: 0 price: 2])
