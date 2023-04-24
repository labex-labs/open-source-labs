# Bst Second Largest

## Problem

Given a binary search tree, find the second largest node in the tree. If the input is None or a single node, an exception should be raised.

To solve this problem, we can traverse the tree in a specific order and keep track of the second largest node we have seen so far. We can start by traversing the right subtree of the root node, and if the right subtree is None, then the largest node is the root node itself. If the right subtree is not None, we can continue traversing the right subtree until we reach a node that does not have a right child. At this point, the largest node in the tree is the parent of this node. If this parent node has a left child, then the second largest node is the largest node in the left subtree of the parent node. If the parent node does not have a left child, then the second largest node is the parent node itself.

## Requirements

The requirements for this challenge are as follows:

- If the input is None or a single node, an exception should be raised.
  - None input should raise a TypeError.
  - Single node input should raise a ValueError.
- We can assume that we already have a Node class with an insert method.
- We can assume that this problem fits memory.

## Example Usage

Here are some examples of how to use this function:

- None or single node -> Exception

<pre>
Input:
                _10_
              _/    \_          
             5        15
            / \       / \
           3   8     12  20
          /     \         \
         2       4        30

Output: 20

Input:
                 10
                 /  
                5
               / \
              3   7
Output: 7
</pre>
