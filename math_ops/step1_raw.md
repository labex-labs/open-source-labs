# Math Ops

Problem: Create a class with an insert method to insert an int to a list. It should also support calculating the max, min, mean, and mode in O(1).

## Requirements

- Can we assume the inputs are valid?
  - No
- Is there a range of inputs?
  - 0 <= item <= 100
- Should mean return a float?
  - Yes
- Should the other results return an int?
  - Yes
- If there are multiple modes, what do we return?
  - Any of the modes
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> TypeError
- [] -> ValueError
- [5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
  - max: 9
  - min: 2
  - mean: 55
  - mode: 9 or 2
