This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement the method draw_line(screen, width, x1, x2) where screen is a list of bytes, width is divisible by 8, and x1, x2 are absolute pixel positions.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the inputs are valid?
  - No
- For the output, do we set corresponding bits in screen?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

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

## Algorithm

- Set start offset to x1 % 8
- Set end offset to x2 % 8
- Determine where the first and last full bytes are
  - First full byte = x1 // 8
    - Increment by 1 if start offset != 0
  - Last full byte = x2 // 8
    - Decrement by 1 if end offset != 7
  - Fill the bytes with 1111 1111
- If x1 and x2 are in the same byte

```txt
    x1 = 2
    x2 = 6

    index  0123 4567
    byte   0011 1110

    We want to build left and right masks such that:

    left   0011 1111
    right  1111 1110
    ----------------
           0011 1110  left & right

    Build the left mask:

    left   0000 0001  1
           0100 0000  1 << (8 - x1)
           0011 1111  (1 << (8 - x1)) - 1

    Build the right mask:

    right  0000 0000  1
           0000 0010  1 << (8 - x2 - 1)
           0000 0001  (1 << (8 - x2 - 1) - 1
           1111 1110  ~((1 << (8 - x2 - 1) - 1)

    Combine the left and right masks:

    left   0011 1111
    right  1111 1110
    ----------------
           0011 1110  left & right

    Set screen[x1//8] or screen[x2//8] |= mask
```

- Else

```txt
    If our starting partial byte is:
           0000 1111

    Build start mask:

    start  0000 0001  1
           0001 0000  1 << 1 << start offset
           0000 1111  (1 << 1 << start offset) - 1

    If our ending partial byte is:
           1111 1100

    Build end mask:

    end    1000 0000  0x10000000
           1111 1100  0x10000000 >> end offset

    Set screen[x1//8] |= start mask
    Set screen[x2//8] |= end mask
```

Complexity:

- Time: O(length of screen)
- Space: O(1)

## Code

```python
class BitsScreen(object):

    def draw_line(self, screen, width, x1, x2):
        if None in (screen, width, x1, x2):
            raise TypeError('Invalid argument: None')
        if not screen or not width:
            raise ValueError('Invalid arg: Empty screen or width')
        MAX_BIT_VALUE = len(screen) * 8
        if x1 < 0 or x2 < 0 or x1 >= MAX_BIT_VALUE or x2 >= MAX_BIT_VALUE:
            raise ValueError('Invalid arg: x1 or x2 out of bounds')
        start_bit = x1 % 8
        end_bit = x2 % 8
        first_full_byte = x1 // 8
        if start_bit != 0:
            first_full_byte += 1
        last_full_byte = x2 // 8
        if end_bit != (8 - 1):
            last_full_byte -= 1
        for byte in range(first_full_byte, last_full_byte + 1):
            screen[byte] = int('11111111', base=2)
        start_byte = x1 // 8
        end_byte = x2 // 8
        if start_byte == end_byte:
            left_mask = (1 << (8 - start_bit)) - 1
            right_mask = ~((1 << (8 - end_bit - 1)) - 1)
            mask = left_mask & right_mask
            screen[start_byte] |= mask
        else:
            start_mask = (1 << (8 - start_bit)) - 1
            end_mask = 1 << (8 - end_bit - 1)
            screen[start_byte] |= start_mask
            screen[end_byte] |= end_mask
```

## Unit Test

```python
%%writefile test_draw_line.py
import unittest


class TestBitsScreen(unittest.TestCase):

    def test_draw_line(self):
        bits_screen = BitsScreen()
        screen = []
        for _ in range(20):
            screen.append(int('00000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=68, x2=80)
        self.assertEqual(screen[8], int('00001111', base=2))
        self.assertEqual(screen[9], int('11111111', base=2))
        self.assertEqual(screen[10], int('10000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=2, x2=6)
        self.assertEqual(screen[0], int('00111110', base=2))
        bits_screen.draw_line(screen, width=32, x1=10, x2=13)
        self.assertEqual(screen[1], int('00111100', base=2))
        print('Success: test_draw_line')


def main():
    test = TestBitsScreen()
    test.test_draw_line()


if __name__ == '__main__':
    main()
```

    Overwriting test_draw_line.py

```python
%run -i test_draw_line.py
```

    Success: test_draw_line
