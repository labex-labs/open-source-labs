# Insert M Into N

Problem: Given two 16 bit numbers, n and m, and two indices i, j, insert m into n such that m starts at bit j and ends at bit i.

## Requirements

- Can we assume j > i?
  - Yes
- Can we assume i through j have enough space for m?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None as an input -> Exception
- Negative index for i or j -> Exception
- General case
```txt
i      = 2
j      = 6
n      = 0000 0100 0000 0000
m      = 0000 0000 0001 0011
result = 0000 0100 0100 1100
```
