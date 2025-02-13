# Tree Dfs

## Problem

Implement depth-first traversals (in-order, pre-order, post-order) on a binary tree. For in-order traversal, we visit the left subtree, then the current node, and then the right subtree. For pre-order traversal, we visit the current node, then the left subtree, and then the right subtree. For post-order traversal, we visit the left subtree, then the right subtree, and then the current node.

## Requirements

To complete this challenge, we need to meet the following requirements:

- We can assume we already have a Node class with an insert method.
- When we process each node, we should call an input method `visit_func` on the node.
- We can assume this fits in memory.

## Example Usage

Here are some examples of how to use the DFS algorithm:

### In-Order Traversal

For a binary tree with values 5, 2, 8, 1, and 3, the in-order traversal would be 1, 2, 3, 5, and 8. For a binary tree with values 1, 2, 3, 4, and 5, the in-order traversal would be 1, 2, 3, 4, and 5.

### Pre-Order Traversal

For a binary tree with values 5, 2, 8, 1, and 3, the pre-order traversal would be 5, 2, 1, 3, and 8. For a binary tree with values 1, 2, 3, 4, and 5, the pre-order traversal would be 1, 2, 3, 4, and 5.

### Post-Order Traversal

For a binary tree with values 5, 2, 8, 1, and 3, the post-order traversal would be 1, 3, 2, 8, and 5. For a binary tree with values 1, 2, 3, 4, and 5, the post-order traversal would be 5, 4, 3, 2, and 1.
