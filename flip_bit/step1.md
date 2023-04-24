# Flip Bit

## Problem

Given a binary number, we need to flip one of its bits from 0 to 1 to maximize the longest sequence of 1s. For example, if we have the binary number `000011110000`, we can flip the fourth bit from 0 to 1 to get `000111110000`, which has a sequence of five 1s. Our goal is to write a Python function that takes in a binary number and returns the length of the longest sequence of 1s after flipping one bit.

## Requirements

The requirements for our Python function are as follows:

- The input must be an integer in base 2.
- We can assume the input is a 32-bit number.
- We do not have to validate the length of the input.
- The output must be an integer.
- We cannot assume the inputs are valid.
- We can assume we are using a positive number since Python doesn't have an >>> operator.
- We can assume this fits memory.

## Example Usage

Here are some examples of how our Python function should behave:

- `None` -> Exception
- `11111111111111111111111111111111` -> 32
- `00000000000000000000000000000000` -> 1
- `00001111110111011111001111110000` -> 10
