# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Given a positive integer, get the next largest number and the next smallest number with the same number of 1's as the given number.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is the output a positive int?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- 0 -> Exception
- negative int -> Exception
- General case:

```txt
    * Input:         0000 0000 1101 0111
    * Next largest:  0000 0000 1101 1011
    * Next smallest: 0000 0000 1100 1111
```

## Algorithm

### get_next_largest

- Find the right-most non trailing zero, call this index
  - We'll use a mask of 1 and do a logical right shift on a copy of num to examine each bit starting from the right
  - Count the number of zeroes to the right of index
    - While num & 1 == 0 and num_copy != 0:
      - Increment number of zeroes
      - Logical shift right num_copy
  - Count the number of ones to the right of index
    - While num & 1 == 1 and num_copy != 0:
      - Increment number of ones
      - Logical shift right num_copy
  - The index will be the sum of number of ones and number of zeroes
  - Set the index bit
  - Clear all bits to the right of index
  - Set bits starting from 0
    - Only set (number of ones - 1) bits because we set index to 1

We should make a note that Python does not have a logical right shift operator built in. We can either use a positive number of implement one for a 32 bit number:

    num % 0x100000000 >> n

### get_next_smallest

- The algorithm for finding the next smallest number is very similar to finding the next largest number
  - Instead of finding the right-most non-trailing zero, we'll find the right most non-trailing one and clear it
  - Clear all bits to the right of index
  - Set bits starting at 0 to the number of ones to the right of index, plus one

Complexity:

- Time: O(b), where b is the number of bits in num
- Space: O(b), where b is the number of bits in num

## Code

```python
class Bits(object):

    def get_next_largest(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num <= 0:
            raise ValueError('num cannot be 0 or negative')
        num_ones = 0
        num_zeroes = 0
        num_copy = num
        # We'll look for index, which is the right-most non-trailing zero
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 0:
            num_zeroes += 1
            num_copy >>= 1
        # Count number of ones to the right of index
        while num_copy != 0 and num_copy & 1 == 1:
            num_ones += 1
            num_copy >>= 1
        # Determine index and set the bit
        index = num_zeroes + num_ones
        num |= 1 << index
        # Clear all bits to the right of index
        num &= ~((1 << index) - 1)
        # Set bits starting from 0
        num |= ((1 << num_ones - 1) - 1)
        return num

    def get_next_smallest(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num <= 0:
            raise ValueError('num cannot be 0 or negative')
        num_ones = 0
        num_zeroes = 0
        num_copy = num
        # We'll look for index, which is the right-most non-trailing one
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 1:
            num_ones += 1
            num_copy >>= 1
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 0:
            num_zeroes += 1
            num_copy >>= 1
        # Determine index and clear the bit
        index = num_zeroes + num_ones
        num &= ~(1 << index)
        # Clear all bits to the right of index
        num &= ~((1 << index) - 1)
        # Set bits starting from 0
        num |= (1 << num_ones + 1) - 1
        return num
```

## Unit Test

```python
%%writefile test_get_next_largest.py
import unittest


class TestBits(unittest.TestCase):

    def test_get_next_largest(self):
        bits = Bits()
        self.assertRaises(Exception, bits.get_next_largest, None)
        self.assertRaises(Exception, bits.get_next_largest, 0)
        self.assertRaises(Exception, bits.get_next_largest, -1)
        num = int('011010111', base=2)
        expected = int('011011011', base=2)
        self.assertEqual(bits.get_next_largest(num), expected)
        print('Success: test_get_next_largest')

    def test_get_next_smallest(self):
        bits = Bits()
        self.assertRaises(Exception, bits.get_next_smallest, None)
        self.assertRaises(Exception, bits.get_next_smallest, 0)
        self.assertRaises(Exception, bits.get_next_smallest, -1)
        num = int('011010111', base=2)
        expected = int('011001111', base=2)
        self.assertEqual(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')

def main():
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()


if __name__ == '__main__':
    main()
```

    Overwriting test_get_next_largest.py

```python
%run -i test_get_next_largest.py
```

    Success: test_get_next_largest
    Success: test_get_next_smallest
