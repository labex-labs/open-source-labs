# Check Balance

## Problem

Given a binary tree, write a Python function to determine if it is balanced. A binary tree is considered balanced if the heights of the two subtrees of any node differ by at most one. The function should take the root node of the binary tree as input and return True if the tree is balanced, and False otherwise. If the input is None, the function should raise an exception.

## Requirements

To solve this problem, we need to meet the following requirements:

- A balanced tree is one where the heights of two subtrees of any node don't differ by more than 1.
- If the input is None, the function should raise an exception.
- We can assume that we already have a Node class with an insert method.
- We can assume that the program fits memory.

## Example Usage

Here are some examples of how the function should behave:

- None -> raise an exception
- 1 -> True
- 5, 3, 8, 1, 4 -> True
- 5, 3, 8, 9, 10 -> False
