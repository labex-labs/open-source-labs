# Draw Line

Problem: Implement the method draw_line(screen, width, x1, x2) where screen is a list of bytes, width is divisible by 8, and x1, x2 are absolute pixel positions.

## Requirements

- Can we assume the inputs are valid?
  - No
- For the output, do we set corresponding bits in screen?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- Invalid inputs -> Exception
  - screen is empty
  - width = 0
  - any input param is None
  - x1 or x2 is out of bounds
- General case for len(screen) = 20, width = 32:
  - x1 = 2, x2 = 6
    - screen[0] = int('00111110', base=2)
  - x1 = 68, x2 = 80
    - screen[8], int('00001111', base=2)
    - screen[9], int('11111111', base=2)
    - screen[10], int('10000000', base=2)
