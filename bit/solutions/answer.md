This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement common bit manipulation operations: get_bit, set_bit, clear_bit, clear_bits_msb_to_index, clear_bits_msb_to_lsb, update_bit.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

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

## Algorithm

### get_bit

```txt
indices  7 6 5 4  3 2 1 0  index = 3
--------------------------------------------------
input    1 0 0 0  1 1 1 0  0b10001110
mask     0 0 0 0  1 0 0 0  1 << index
--------------------------------------------------
result   0 0 0 0  1 0 0 0  number & mask != 0
```

Complexity:

- Time: O(n)
- Space: O(n)

### set_bit

```txt
indices  7 6 5 4  3 2 1 0  index = 4
--------------------------------------------------
input    1 0 0 0  1 1 1 0  0b10001110
mask     0 0 0 1  0 0 0 0  1 << index
--------------------------------------------------
result   1 0 0 1  1 1 1 0  number | mask
```

Complexity:

- Time: O(n)
- Space: O(n)

### clear_bit

```txt
indices  7 6 5 4  3 2 1 0  index = 3
--------------------------------------------------
input    1 0 0 0  1 1 1 0  0b10001110
mask     0 0 0 0  1 0 0 0  1 << index
mask     1 1 1 1  0 1 1 1  ~(1 << index)
--------------------------------------------------
result   1 0 0 0  0 1 1 0  number & mask
```

Complexity:

- Time: O(n)
- Space: O(n)

### clear_bits_msb_to_index

```txt
indices  7 6 5 4  3 2 1 0  index = 3
--------------------------------------------------
input    1 0 0 0  1 1 1 0  0b10001110
mask     0 0 0 0  1 0 0 0  1 << index
mask     0 0 0 0  0 1 1 1  (1 << index) - 1
--------------------------------------------------
result   0 0 0 0  0 1 1 1  number & mask
```

Complexity:

- Time: O(n)
- Space: O(n)

### clear_bits_index_to_lsb

```txt
indices  7 6 5 4  3 2 1 0  index = 3
--------------------------------------------------
input    1 0 0 0  1 1 1 0  0b10001110
mask     0 0 0 1  0 0 0 0  1 << index + 1
mask     0 0 0 0  1 1 1 1  (1 << index + 1) - 1
mask     1 1 1 1  0 0 0 0  ~((1 << index + 1) - 1)
--------------------------------------------------
result   1 0 0 0  0 0 0 0  number & mask
```

Complexity:

- Time: O(n)
- Space: O(n)

### update_bit

- Use `get_bit` to see if the value is already set or cleared
- If not, use `set_bit` if setting the value or `clear_bit` if clearing the value

Complexity:

- Time: O(n)
- Space: O(n)

## Code

```python
def validate_index(func):
    def validate_index_wrapper(self, *args, **kwargs):
        for arg in args:
            if arg < 0:
                raise IndexError('Invalid index')
        return func(self, *args, **kwargs)
    return validate_index_wrapper
```

```python
class Bit(object):

    def __init__(self, number):
        if number is None:
            raise TypeError('number cannot be None')
        self.number = number

    @validate_index
    def get_bit(self, index):
        mask = 1 << index
        return self.number & mask != 0

    @validate_index
    def set_bit(self, index):
        mask = 1 << index
        self.number |= mask
        return self.number

    @validate_index
    def clear_bit(self, index):
        mask = ~(1 << index)
        self.number &= mask
        return self.number

    @validate_index
    def clear_bits_msb_to_index(self, index):
        mask = (1 << index) - 1
        self.number &= mask
        return self.number

    @validate_index
    def clear_bits_index_to_lsb(self, index):
        mask = ~((1 << index + 1) - 1)
        self.number &= mask
        return self.number

    @validate_index
    def update_bit(self, index, value):
        if value is None or value not in (0, 1):
            raise Exception('Invalid value')
        if self.get_bit(index) == value:
            return self.number
        if value:
            self.set_bit(index)
        else:
            self.clear_bit(index)
        return self.number
```

## Unit Test

```python
%%writefile test_bit.py
import unittest


class TestBit(unittest.TestCase):

    def test_bit(self):
        number = int('10001110', base=2)
        bit = Bit(number)
        self.assertEqual(bit.get_bit(index=3), True)
        expected = int('10011110', base=2)
        self.assertEqual(bit.set_bit(index=4), expected)
        bit = Bit(number)
        expected = int('10000110', base=2)
        self.assertEqual(bit.clear_bit(index=3), expected)
        bit = Bit(number)
        expected = int('00000110', base=2)
        self.assertEqual(bit.clear_bits_msb_to_index(index=3), expected)
        bit = Bit(number)
        expected = int('10000000', base=2)
        self.assertEqual(bit.clear_bits_index_to_lsb(index=3), expected)
        bit = Bit(number)
        self.assertEqual(bit.update_bit(index=3, value=1), number)
        bit = Bit(number)
        expected = int('10000110', base=2)
        self.assertEqual(bit.update_bit(index=3, value=0), expected)
        bit = Bit(number)
        expected = int('10001111', base=2)
        self.assertEqual(bit.update_bit(index=0, value=1), expected)
        print('Success: test_bit')


def main():
    test = TestBit()
    test.test_bit()


if __name__ == '__main__':
    main()
```

    Overwriting test_bit.py

```python
%run -i test_bit.py
```

    Success: test_bit
