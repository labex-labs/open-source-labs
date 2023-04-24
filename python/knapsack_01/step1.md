# Knapsack 01

## Problem

Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine which items to select to maximize total value. The problem is known as the 0/1 knapsack problem because each item can only be selected once (0/1 decision). The problem is NP-hard, which means that there is no known polynomial-time algorithm that can solve it optimally for all cases.

## Requirements

To solve the Knapsack problem, we need to consider the following requirements:

- The items cannot be replaced once they are placed in the knapsack.
- We cannot split an item.
- We cannot have an input item with weight or value of 0.
- We cannot assume that the inputs are valid.
- The inputs should be sorted by val/weight.
- We can assume that the problem fits memory.

## Example

Here is an example of how to use the Knapsack algorithm:

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

In this example, we have a knapsack with a total weight capacity of 8 and four items with their respective values and weights. We need to select the items that maximize the total value while keeping the weight within the capacity of the knapsack. The optimal solution is to select items b and d, which have a total value of 13 and a total weight of 7.
