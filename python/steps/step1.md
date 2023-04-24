# Python Challenge: Steps

## Problem

Imagine you are standing at the bottom of a staircase with n steps. You can take a single, double, or triple step at a time. The problem is to find out how many possible ways there are to run up to the nth step.

For example, if there are 3 steps, you can run up the stairs in the following ways:

- 1-1-1
- 1-2
- 2-1
- 3

So, there are 4 possible ways to run up to the 3rd step.

## Requirements

To solve this problem, we need to keep in mind the following requirements:

- If n == 0, the result should be 1. However, there are different approaches to this problem, which can be discussed.
- We cannot assume that the inputs are valid.
- We can assume that the problem fits memory.

## Example Usage

Here are some examples of how this problem can be solved using Python:

- None or negative input -> Exception
- n == 0 -> 1
- n == 1 -> 1
- n == 2 -> 2
- n == 3 -> 4
- n == 4 -> 7
- n == 10 -> 274
