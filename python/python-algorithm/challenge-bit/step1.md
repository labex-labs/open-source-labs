# Bit Manipulation Operations

## Problem

Implement the following common bit manipulation operations in Python:

- `get_bit`: Given a number and an index, return the value of the bit at the given index.
- `set_bit`: Given a number and an index, set the value of the bit at the given index to 1.
- `clear_bit`: Given a number and an index, set the value of the bit at the given index to 0.
- `clear_bits_msb_to_index`: Given a number and an index, set all bits from the most significant bit to the given index to 0.
- `clear_bits_index_to_lsb`: Given a number and an index, set all bits from the given index to the least significant bit to 0.
- `update_bit`: Given a number, an index, and a value, update the value of the bit at the given index to the given value.

## Requirements

The implementation should meet the following requirements:

- The inputs may not be valid, and the implementation should handle such cases gracefully.
- The implementation should fit memory.

## Example Usage

Here are some examples of how to use the implemented functions:

- `get_bit`:
  ```
  number   = 0b10001110
  index = 3
  expected = True
  ```
- `set_bit`:
  ```
  number   = 0b10001110
  index = 4
  expected = 0b10011110
  ```
- `clear_bit`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000110
  ```
- `clear_bits_msb_to_index`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b00000110
  ```
- `clear_bits_index_to_lsb`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000000
  ```
- `update_bit`:

  ```
  number   = 0b10001110
  index = 3
  value = 1
  expected = 0b10001110

  number   = 0b10001110
  index = 3
  value = 0
  expected = 0b10000110

  number   = 0b10001110
  index = 0
  value = 1
  expected = 0b10001111
  ```
