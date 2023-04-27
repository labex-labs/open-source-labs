# Print Binary

Problem: Given a real number between 0 and 1, print the binary representation. If the length of the representation is > 32, return 'ERROR'.

## Requirements

- Is the input a float?
  - Yes
- Is the output a string?
  - Yes
- Is 0 and 1 inclusive?
  - No
- Does the result include a trailing zero and decimal point?
  - Yes
- Is the leading zero and decimal point counted in the 32 char limit?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> 'ERROR'
- Out of bounds (0, 1) -> 'ERROR'
- General case
  - 0.625 -> 0.101
  - 0.987654321 -> 'ERROR'
