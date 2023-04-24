# Remove Duplicates

## Problem

Given a non-circular, singly linked list, remove duplicates from it. The goal is to modify the original list in place and return the head of the modified list.

## Requirements

To solve this problem, we need to consider the following requirements:

- The linked list is non-circular and singly linked.
- None values cannot be inserted in the list.
- We already have a linked list class that can be used for this problem.
- Two solutions need to be implemented: one using additional data structures and one without.
- The problem fits in memory.

## Example Usage

Here are some examples of how the function should behave:

- Empty linked list -> []
- One element linked list -> [element]
- General case with no duplicates -> [1, 2, 3, 4]
- General case with duplicates -> [1, 2, 3]
