# Get Next

## Problem

Given a positive integer, you need to find the next largest number and the next smallest number with the same number of 1's as the given number. For example, if the input is 0000 0000 1101 0111, the output should be 0000 0000 1101 1011 for the next largest number and 0000 0000 1100 1111 for the next smallest number.

## Requirements

To solve this challenge, you need to meet the following requirements:

- The output should be a positive integer.
- The inputs may not be valid, so you need to handle exceptions.
- The solution should fit in memory.

## Example Usage

Here are some examples of how to use this function:

- None -> Exception
- 0 -> Exception
- negative int -> Exception
- General case:
<pre>
    * Input:         0000 0000 1101 0111
    * Next largest:  0000 0000 1101 1011
    * Next smallest: 0000 0000 1100 1111
</pre>
