# Tree Height

## Problem

Given a binary tree, write a Python function to determine the height of the tree. The height of a binary tree is the length of the longest path from the root node to any leaf node in the tree.

## Requirements

To solve this problem, we need to meet the following requirements:

- The given tree is a binary tree.
- We already have a Node class with an insert method.
- The solution fits memory.

## Example Usage

Here are some examples of how the function should behave:

- If the tree has only one node, the height is 1. For example, if the input is 5 -> 1, the output should be 1.
- If the tree has multiple nodes, the height is the length of the longest path from the root node to any leaf node. For example, if the input is 5, 2, 8, 1, 3 -> 3, the output should be 3.
