# Longest Increasing Subsequence

## Problem

Given a sequence of integers, find the longest increasing subsequence. The subsequence can be non-contiguous and may contain duplicates. If there are multiple solutions, return any one.

## Requirements

To solve this problem, we need to consider the following requirements:

- Are duplicates possible?
  - Yes
- Can we assume the inputs are integers?
  - Yes
- Can we assume the inputs are valid?
  - No, we need to handle invalid inputs.
- Do we expect the result to be an array of the longest increasing subsequence?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

Here are some examples of how this function can be used:

- None -> Exception
- [] -> []
- [3, 4, -1, 0, 6, 2, 3] -> [-1, 0, 2, 3]
