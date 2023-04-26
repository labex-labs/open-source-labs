# Knapsack Unbounded

Problem: Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine the max total value you can carry.

## Requirements

- Can we replace the items once they are placed in the knapsack?
  - Yes, this is the unbounded knapsack problem
- Can we split an item?
  - No
- Can we get an input item with weight of 0 or value of 0?
  - No
- Do we need to return the items that make up the max total value?
  - No, just the total value
- Can we assume the inputs are valid?
  - No
- Are the inputs in sorted order by val/weight?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- items or total weight is None -> Exception
- items or total weight is 0 -> 0
- General case

```txt
total_weight = 8
items
  v | w
  0 | 0
a 1 | 1
b 3 | 2
c 7 | 4

max value = 14
```
