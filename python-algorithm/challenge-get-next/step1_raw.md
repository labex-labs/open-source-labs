# Get Next

Problem: Given a positive integer, get the next largest number and the next smallest number with the same number of 1's as the given number.

## Requirements

- Is the output a positive int?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> Exception
- 0 -> Exception
- negative int -> Exception
- General case:

```txt
    * Input:         0000 0000 1101 0111
    * Next largest:  0000 0000 1101 1011
    * Next smallest: 0000 0000 1100 1111
```
