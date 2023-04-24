# Bst Successor

## Problem

Given a binary search tree and a node in it, find the in-order successor of that node. The successor of a node is the node that appears immediately after the given node in an in-order traversal of the tree. If there is no successor, return None. If the input is None, throw an exception. We can assume we already have a Node class that keeps track of parents, and we can assume this fits memory.

## Requirements

- The function should return the in-order successor of a given node in a binary search tree.
- If there is no successor, the function should return None.
- If the input is None, the function should throw an exception.
- We can assume we already have a Node class that keeps track of parents.
- We can assume this fits memory.

## Example Usage

<pre>
          _5_
        /     \
       3       8
      / \    /   \
     2   4  6    12
    /        \   / \
   1          7 10  15
               /
              9

In: None  Out: Exception
In: 4     Out: 5
In: 5     Out: 6
In: 8     Out: 9
In: 15    Out: None
</pre>
