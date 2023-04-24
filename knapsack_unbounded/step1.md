# Knapsack Unbounded

## Problem

Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine the maximum total value you can carry. The items can be selected multiple times.

## Requirements

To solve the Knapsack Unbounded problem, the following requirements must be met:

- The items can be replaced once they are placed in the knapsack.
- An item cannot be split.
- The input items cannot have a weight or value of 0.
- Only the total value needs to be returned, not the items that make up the max total value.
- The inputs may not be valid, so validation is required.
- The inputs are sorted by val/weight.
- Memory constraints are not an issue.

## Example Usage

The Knapsack Unbounded problem can be used in various scenarios, such as resource allocation and financial portfolio optimization. Here are some examples of how it can be used:

- If the total weight or items are None, an exception should be raised.
- If the total weight or items are 0, the result should be 0.
- For a general case, suppose the total weight is 8 and the items are:

  | v   | w   |
  | --- | --- |
  | 0   | 0   |
  | 1   | 1   |
  | 3   | 2   |
  | 7   | 4   |

  The maximum value that can be carried is 14.
