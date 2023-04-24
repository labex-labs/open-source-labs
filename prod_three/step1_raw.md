# Prod Three

Problem: Find the highest product of three numbers in a list.

## Requirements

- Is the input a list of integers?
  - Yes
- Can we get negative inputs?
  - Yes
- Can there be duplicate entries in the input?
  - Yes
- Will there always be at least three integers?
  - No
- Can we assume the inputs are valid?
  - No, check for None input
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> TypeError
- Less than three ints -> ValueError
- [5, -2, 3] -> -30
- [5, -2, 3, 1, -1, 4] -> 60
