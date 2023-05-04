# Kth To Last Elem

Problem: Find the kth to last element of a linked list.

## Requirements

- Can we assume this is a non-circular, singly linked list?
  - Yes
- Can we assume k is a valid integer?
  - Yes
- If k = 0, does this return the last element?
  - Yes
- What happens if k is greater than or equal to the length of the linked list?
  - Return None
- Can you use additional data structures?
  - No
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes

## Example Usage

- Empty list -> None
- k is >= the length of the linked list -> None
- One element, k = 0 -> element
- General case with many elements, k < length of linked list
