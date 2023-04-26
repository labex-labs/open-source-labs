# Knapsack 01

Problem: Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine which items to select to maximize total value.

## Requirements

- Can we replace the items once they are placed in the knapsack?
  - No, this is the 0/1 knapsack problem
- Can we split an item?
  - No
- Can we get an input item with weight of 0 or value of 0?
  - No
- Can we assume the inputs are valid?
  - No
- Are the inputs in sorted order by val/weight?
  - Yes, if not we'd need to sort them first
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
a 2 | 2
b 4 | 2
c 6 | 4
d 9 | 5

max value = 13
items
  v | w
b 4 | 2
d 9 | 5 
```
