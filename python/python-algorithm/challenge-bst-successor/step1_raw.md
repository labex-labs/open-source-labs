# Bst Successor

Problem: Find the in-order successor of a given node in a binary search tree.

## Requirements

- If there is no successor, do we return None?
  - Yes
- If the input is None, should we throw an exception?
  - Yes
- Can we assume we already have a Node class that keeps track of parents?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

```txt
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
```
