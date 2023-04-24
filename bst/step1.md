# Bst

## Problem

A binary search tree is a data structure that allows fast search, insert, and delete operations. It is a tree where each node has at most two children, and the left child is less than the parent, and the right child is greater than the parent. The insert method adds a new node to the tree in the appropriate position based on its value.

Your task is to implement a binary search tree with an insert method in Python. The insert method should take a value and add a new node to the tree in the appropriate position based on its value. If the root input is None, return a tree with the only element being the new root node.

## Requirements

To complete this challenge, you need to meet the following requirements:

- You cannot insert None values.
- You can assume you are working with valid integers.
- You can assume all left descendents are less than or equal to the node, and all right descendents are greater than the node.
- You do not have to keep track of the parent nodes, but it is optional.
- You can assume this fits in memory.

## Example Usage

### Insert

Insert will be tested through the following traversal:

### In-Order Traversal

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

You do not have to code the in-order traversal, it is part of the unit test.
