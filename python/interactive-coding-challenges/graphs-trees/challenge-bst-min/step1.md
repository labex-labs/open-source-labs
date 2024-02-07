# Bst Min

## Problem

Given a sorted array, we need to create a binary search tree with minimal height. The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. The goal is to create a binary search tree with the minimum possible height.

## Requirements

To solve this problem, we need to meet the following requirements:

- The array must be in increasing order.
- The array elements must be unique.
- We must assume that we already have a Node class with an insert method.
- We must assume that this fits memory.

## Example Usage

Here are some examples of how to use the function:

- Input: [0, 1, 2, 3, 4, 5, 6]
  Output: A binary search tree with height 3

- Input: [0, 1, 2, 3, 4, 5, 6, 7]
  Output: A binary search tree with height 4
