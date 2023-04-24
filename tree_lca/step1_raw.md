# Tree Lca

Problem: Find the lowest common ancestor in a binary tree.

## Requirements

- Is this a binary search tree?
  - No
- Can we assume the two nodes are in the tree?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

<pre>
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
</pre>

- 0, 5 -> None
- 5, 0 -> None
- 1, 8 -> 3
- 12, 8 -> 5
- 12, 40 -> 10
- 9, 20 -> 9
- 3, 5 -> 5
