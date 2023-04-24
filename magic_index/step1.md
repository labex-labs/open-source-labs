# Magic Index

## Problem

Given a sorted array of integers with possible duplicates, write a Python function to find the magic index, if one exists, in the array. If there are multiple magic values, return the left-most one. If there is no magic index, return -1.

## Requirements

To solve the problem, the following requirements must be met:

- The array is sorted.
- The elements in the array may not be distinct.
- Negative values are allowed in the array.
- If there is no magic index, return -1.

## Example Usage

The following examples illustrate the usage of the function:

- None input -> -1
- Empty array -> -1

<pre>
a[i]  -4 -2  2  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
</pre>

Result: 2

<pre>
a[i]  -4 -2  1  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
</pre>

Result: 6

<pre>
a[i]  -4 -2  1  6  6  6  7 10
  i    0  1  2  3  4  5  6  7
</pre>

Result: -1
