# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Given a real number between 0 and 1, print the binary representation. If the length of the representation is > 32, return 'ERROR'.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is the input a float?
  - Yes
- Is the output a string?
  - Yes
- Is 0 and 1 inclusive?
  - No
- Does the result include a trailing zero and decimal point?
  - Yes
- Is the leading zero and decimal point counted in the 32 char limit?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> 'ERROR'
- Out of bounds (0, 1) -> 'ERROR'
- General case
  - 0.625 -> 0.101
  - 0.987654321 -> 'ERROR'

## Algorithm

- Set the result to '0.'
- Start with a fraction of 0.5, which is 0.1 in base 2
- Loop while num > 0
  - Check num versus fraction
    - If num > fraction, add a 1 to the result, num -= fraction
    - Else, add a 0 to the result
    - If the len(result) > 32, return 'ERROR'

Complexity:

- Time: O(1)
- Space: O(1)

## Code

```python
from __future__ import division


class Bits(object):

    MAX_BITS = 32

    def print_binary(self, num):
        if num is None or num >= 1 or num <= 0:
            return 'ERROR'
        result = ['0', '.']
        fraction = 0.5
        while num:
            if num >= fraction:
                result.append('1')
                num -= fraction
            else:
                result.append('0')
            if len(result) > self.MAX_BITS:
                return 'ERROR'
            fraction /= 2
        return ''.join(result)
```

## Unit Test

```python
%%writefile test_print_binary.py
import unittest


class TestBits(unittest.TestCase):

    def test_print_binary(self):
        bit = Bits()
        self.assertEqual(bit.print_binary(None), 'ERROR')
        self.assertEqual(bit.print_binary(0), 'ERROR')
        self.assertEqual(bit.print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        self.assertEqual(bit.print_binary(num), expected)
        num = 0.987654321
        self.assertEqual(bit.print_binary(num), 'ERROR')
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_print_binary()


if __name__ == '__main__':
    main()
```

    Overwriting test_print_binary.py

```python
%run -i test_print_binary.py
```

    Success: test_print_binary
