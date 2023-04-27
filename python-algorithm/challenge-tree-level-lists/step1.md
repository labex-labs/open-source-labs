# Tree Level Lists

## Problem

Given a binary search tree, create a list for each level of the tree. Each list should contain the nodes at that level of the tree. The lists should be returned in an array of arrays, where each subarray represents a level of the tree.

## Requirements

To solve this problem, the following requirements must be met:

- The given tree is a binary search tree.
- Each level of the tree should be represented by a list of nodes.
- A Node class with an insert method is already provided.
- The solution should fit in memory.

## Example Usage

For example, given the binary search tree with the following values:

```
5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11
```

The function should return the following array of arrays:

```
[[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
```

Note that each number in the result is actually a node containing the number.
