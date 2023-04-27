# Bst Second Largest

Problem: Find the second largest node in a binary search tree.

## Requirements

- If this is called on a None input or a single node, should we raise an exception?
  - Yes
    - None -> TypeError
    - Single node -> ValueError
- Can we assume we already have a Node class with an insert method?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- None or single node -> Exception

```txt
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
```
