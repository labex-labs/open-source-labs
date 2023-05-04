# Merge Into

Problem: Given sorted arrays A, B, merge B into A in sorted order.

## Requirements

- Does A have enough space for B?
  - Yes
- Can the inputs have duplicate array items?
  - Yes
- Can we assume the inputs are valid?
  - No
- Does the inputs also include the actual size of A and B?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- A or B is None -> Exception
- index of last A or B < 0 -> Exception
- A or B is empty
- General case
  - A = [1, 3, 5, 7, 9, None, None, None]
  - B = [4, 5, 6]
  - A = [1, 3, 4, 5, 5, 6, 7, 9]
