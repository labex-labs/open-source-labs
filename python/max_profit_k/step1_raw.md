# Max Profit K

Problem: Given a list of stock prices on each consecutive day, determine the max profits with k transactions.

## Requirements

- Is k the number of sell transactions?
  - Yes
- Can we assume the prices input is an array of ints?
  - Yes
- Can we assume the inputs are valid?
  - No
- If the prices are all decreasing and there is no opportunity to make a profit, do we just return 0?
  - Yes
- Should the output be the max profit and days to buy and sell?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

```txt
* Prices: None or k: None -> None
* Prices: [] or k <= 0 -> []
* Prices: [0, -1, -2, -3, -4, -5]
    * (max profit, list of transactions)
    * (0, [])
* Prices: [2, 5, 7, 1, 4, 3, 1, 3] k: 3
    * (max profit, list of transactions)
    * (10, [Type.SELL day: 7 price: 3, 
            Type.BUY  day: 6 price: 1, 
            Type.SELL day: 4 price: 4, 
            Type.BUY  day: 3 price: 1, 
            Type.SELL day: 2 price: 7, 
            Type.BUY  day: 0 price: 2])
```
