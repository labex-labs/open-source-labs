# Pairwise Swap

Problem: Swap the odd and even bits of a positive integer with as few operations as possible.

## Requirements

- Can we assume the input is always a positive int?
  - Yes
- Can we assume we're working with 32 bits?
  - Yes
- Is the output an int?
  - Yes
- Can we assume the inputs are valid (not None)?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> Exception
- 0 -> 0
- -1 -> -1
- General case
<pre>
    input  = 1001 1111 0110
    result = 0110 1111 1001
<pre>
