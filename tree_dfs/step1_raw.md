# Tree Dfs

Problem: Implement depth-first traversals (in-order, pre-order, post-order) on a binary tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Requirements

- Can we assume we already have a Node class with an insert method?
  - Yes
- What should we do with each node when we process it?
  - Call an input method `visit_func` on the node
- Can we assume this fits in memory?
  - Yes

## Example Usage

### In-Order Traversal

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

### Pre-Order Traversal

- 5, 2, 8, 1, 3 -> 5, 2, 1, 3, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

### Post-Order Traversal

- 5, 2, 8, 1, 3 -> 1, 3, 2, 8, 5
- 1, 2, 3, 4, 5 -> 5, 4, 3, 2, 1
