# Tree BFS

## Problem

Given a binary tree, implement a function that performs a breadth-first traversal on the tree. The function should call an input method `visit_func` on each node when it is processed.

## Requirements

To solve this problem, the following requirements must be met:

- A Node class with an insert method is already available.
- The solution should fit in memory.
- The `visit_func` method should be called on each node when it is processed.

## Example

### Breadth-First Traversal

Suppose we have a binary tree with the following structure:

```
    5
   / \
  2   8
 / \
1   3
```

Performing a breadth-first traversal on this tree would result in the following sequence of nodes being visited: `5, 2, 8, 1, 3`.
