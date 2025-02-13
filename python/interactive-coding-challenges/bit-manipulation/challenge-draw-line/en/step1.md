# Draw Line

## Problem

Implement the method `draw_line(screen, width, x1, x2)` where `screen` is a list of bytes, `width` is divisible by 8, and `x1`, `x2` are absolute pixel positions. The method should set the corresponding bits in `screen` to draw a line from `x1` to `x2`.

### Requirements

The implementation of `draw_line` must meet the following requirements:

- The inputs may not be assumed to be valid.
- The corresponding bits in `screen` must be set to draw the line.
- It may be assumed that the implementation fits memory.

## Example Usage

The following examples illustrate the expected behavior of `draw_line`:

- Invalid inputs -> Exception
  - `screen` is empty
  - `width` = 0
  - any input param is `None`
  - `x1` or `x2` is out of bounds
- General case for `len(screen)` = 20, `width` = 32:
  - `x1` = 2, `x2` = 6
    - `screen[0]` = `int('00111110', base=2)`
  - `x1` = 68, `x2` = 80
    - `screen[8]`, `int('00001111', base=2)`
    - `screen[9]`, `int('11111111', base=2)`
    - `screen[10]`, `int('10000000', base=2)`
