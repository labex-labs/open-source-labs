# Bst

Problem: Implement a binary search tree with an insert method.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Requirements

- Can we insert None values?
  - No
- Can we assume we are working with valid integers?
  - Yes
- Can we assume all left descendents <= n < all right descendents?
  - Yes
- Do we have to keep track of the parent nodes?
  - This is optional
- Can we assume this fits in memory?
  - Yes

## Example Usage

### Insert

Insert will be tested through the following traversal:

### In-Order Traversal

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

If the `root` input is `None`, return a tree with the only element being the new root node.

You do not have to code the in-order traversal, it is part of the unit test.
