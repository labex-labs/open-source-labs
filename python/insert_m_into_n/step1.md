# Insert M Into N

## Problem

Given two 16-bit numbers, `n` and `m`, and two indices `i` and `j`, insert `m` into `n` such that `m` starts at bit `j` and ends at bit `i`. The program should handle the following cases:

- If none is given as an input, an exception should be raised.
- If a negative index is given for `i` or `j`, an exception should be raised.
- If the inputs are invalid, an exception should be raised.
- If `i` through `j` do not have enough space for `m`, an exception should be raised.

The program should return the resulting 16-bit number after the insertion.

## Requirements

The program should meet the following requirements:

- `j` should be greater than `i`.
- `i` through `j` should have enough space for `m`.
- The inputs should be valid.
- The program should fit in memory.

## Example Usage

Here is an example of the program's usage:

```txt
i      = 2
j      = 6
n      = 0000 0100 0000 0000
m      = 0000 0000 0001 0011
result = 0000 0100 0100 1100
```

In this example, `m` is inserted into `n` such that `m` starts at bit `j=6` and ends at bit `i=2`. The resulting 16-bit number is `0000 0100 0100 1100`.
