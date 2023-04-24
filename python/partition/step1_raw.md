# Partition

Problem: Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

## Requirements

- Can we assume this is a non-circular, singly linked list?
  - Yes
- Do we expect the function to return a new list?
  - Yes
- Can we assume the input x is valid?
  - Yes
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes
- Can we create additional data structures?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Example Usage

- Empty list -> []
- One element list -> [element]
- Left linked list is empty
- Right linked list is empty
- General case
  - Partition = 10
  - Input: 4, 3, 7, 8, 10, 1, 10, 12
  - Output: 4, 3, 7, 8, 1, 10, 10, 12
