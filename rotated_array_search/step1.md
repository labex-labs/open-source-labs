# Rotated Array Search

## Problem

Given a sorted array that has been rotated a number of times, we need to find a specific element in the array. For example, if the original sorted array was [1, 2, 3, 4, 5] and it was rotated twice to become [3, 4, 5, 1, 2], we need to find the index of a specific element, such as 4.

## Requirements

To solve this problem, we need to consider the following requirements:

- The input is an array of integers.
- We do not know how many times the array was rotated.
- The array was originally sorted in increasing order.
- For the output, we need to return the index of the element we are searching for.
- We cannot assume that the inputs are valid.
- We can assume that the solution fits memory.

## Example Usage

Here are some examples of how this function can be used:

- If no input is provided, an exception should be raised.
- If an empty array is provided, None should be returned.
- If the element we are searching for is not found in the array, None should be returned.
- If the array contains duplicates, the function should still be able to find the correct index.
- If the array does not contain duplicates, the function should still be able to find the correct index.
