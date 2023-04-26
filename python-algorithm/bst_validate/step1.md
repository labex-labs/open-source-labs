# Bst Validate

## Problem

The problem is to write a Python function that takes the root node of a binary tree as input and determines if it is a valid binary search tree. A binary tree is a valid binary search tree if and only if the following conditions are met:

1. The left subtree of a node contains only nodes with values less than the node's value.
2. The right subtree of a node contains only nodes with values greater than the node's value.
3. Both the left and right subtrees are themselves valid binary search trees.

## Requirements

To solve this challenge, the following requirements must be met:

- The function should be able to handle binary trees with duplicates.
- If the function is called with a None input, it should raise an exception.
- The Node class should already be defined.
- The binary tree should fit in memory.

## Example Usage

```txt
Valid:
      5
    /   \
   5     8
  /     /
 4     6
        \
         7

Invalid:
      5
    /   \
   5     8
  / \   /
 4   9 7
```
