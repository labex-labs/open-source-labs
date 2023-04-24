# Invert Tree

## Problem

Given a binary tree, write a function to invert the tree. The function should take the root node of the tree as input and return the new root node of the inverted tree.

## Requirements

To solve this problem, you need to meet the following requirements:

- You should have a Node class that represents a node in the binary tree.
- You should swap all left and right node pairs in the binary tree.
- You should handle invalid inputs gracefully.
- Your solution should fit in memory.

## Example Usage

Suppose we have the following binary tree:

<pre>
     5
   /   \
  2     7
 / \   / \
1   3 6   9
</pre>

After inverting the tree, we should get:

<pre>
     5
   /   \
  7     2
 / \   / \
9   6 3   1
</pre>
