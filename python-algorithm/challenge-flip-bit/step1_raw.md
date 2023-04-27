# Flip Bit

Problem: Flip one bit from 0 to 1 to maximize the longest sequence of 1s.

## Requirements

- Is the input an int, base 2?
  - Yes
- Can we assume the input is a 32 bit number?
  - Yes
- Do we have to validate the length of the input?
  - No
- Is the output an int?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume we are using a positive number since Python doesn't have an >>> operator?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> Exception
- All 1's -> Count of 1s
- All 0's -> 1
- General case
  - 0000 1111 1101 1101 1111 0011 1111 0000 -> 10 (ten)
