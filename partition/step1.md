# Partition

## Problem

Given a singly linked list, partition it around a value x, such that all nodes less than x come before all nodes greater than or equal to x. The function should return a new linked list.

## Requirements

To solve this problem, we need to consider the following requirements:

- The linked list is non-circular and singly linked.
- The function should return a new linked list.
- The input value x is valid.
- We already have a linked list class that can be used for this problem.
- We can create additional data structures.
- The problem fits in memory.

## Example Usage

Here are some examples of how the function should work:

- Empty list -> []
- One element list -> [element]
- Left linked list is empty -> [10, 11, 12]
- Right linked list is empty -> [1, 2, 3]
- General case
  - Partition = 10
  - Input: 4, 3, 7, 8, 10, 1, 10, 12
  - Output: 4, 3, 7, 8, 1, 10, 10, 12
