# Tree Lca

## Problem

Given a binary tree and two nodes, find their lowest common ancestor.

## Requirements

To solve this problem, we need to consider the following requirements:

- The given tree is a binary tree, not a binary search tree.
- We cannot assume that the two nodes are already in the tree.
- We can assume that the binary tree fits in memory.

## Example Usage

Consider the following binary tree:

<pre>
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
</pre>

We can test our function with the following inputs and expected outputs:

- 0, 5 -> None (both nodes are not in the tree)
- 5, 0 -> None (both nodes are not in the tree)
- 1, 8 -> 3
- 12, 8 -> 5
- 12, 40 -> 10
- 9, 20 -> 9
- 3, 5 -> 5
