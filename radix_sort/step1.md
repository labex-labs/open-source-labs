# Radix Sort

## Problem

Implement radix sort algorithm to sort a list of integers. The algorithm sorts the integers by comparing their digits starting from the least significant digit to the most significant digit. The algorithm first sorts the integers based on the least significant digit, then the second least significant digit, and so on until the most significant digit is sorted.

## Requirements

To implement radix sort, the following requirements must be met:

- The input must be a list of integers.
- Check for None in place of an array.
- Assume array elements are integers.
- The digits must be base 10.
- The algorithm must be able to handle any number of digits.
- The algorithm must fit in memory.

## Example Usage

The following are examples of how to use the radix sort algorithm:

- None -> Exception
- [] -> []
- [128, 256, 164, 8, 2, 148, 212, 242, 244] -> [2, 8, 128, 148, 164, 212, 242, 244, 256]
