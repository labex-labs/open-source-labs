# Merge Ranges

Problem: Given a list of tuples representing ranges, condense the ranges.

Example: [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]

## Requirements

- Are the tuples in sorted order?
  - No
- Are the tuples ints?
  - Yes
- Will all tuples have the first element less than the second?
  - Yes
- Is there an upper bound on the input range?
  - No
- Is the output a list of tuples?
  - Yes
- Is the output a new array?
  - Yes
- Can we assume the inputs are valid?
  - No, check for None
- Can we assume this fits memory?
  - Yes

## Example Usage

```txt
* None input -> TypeError
* [] - []
* [(2, 3), (7, 9)] -> [(2, 3), (7, 9)]
* [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]
* [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)] -> [(1, 11)]
* [(2, 3), (3, 8), (7, 9), (8, 10)] -> [(2, 10)]
```
