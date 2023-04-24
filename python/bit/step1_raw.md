# Bit

Problem: Implement common bit manipulation operations: get_bit, set_bit, clear_bit, clear_bits_msb_to_index, clear_bits_msb_to_lsb, update_bit.

## Requirements

- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None as a number input -> Exception
- Negative index -> Exception

### get_bit

    number   = 0b10001110, index = 3
    expected = True

### set_bit

    number   = 0b10001110, index = 4
    expected = 0b10011110

### clear_bit

    number   = 0b10001110, index = 3
    expected = 0b10000110

### clear_bits_msb_to_index

    number   = 0b10001110, index = 3
    expected = 0b00000110

### clear_bits_index_to_lsb

    number   = 0b10001110, index = 3
    expected = 0b10000000

### update_bit

    number   = 0b10001110, index = 3, value = 1
    expected = 0b10001110
    number   = 0b10001110, index = 3, value = 0
    expected = 0b10000110
    number   = 0b10001110, index = 0, value = 1
    expected = 0b10001111
