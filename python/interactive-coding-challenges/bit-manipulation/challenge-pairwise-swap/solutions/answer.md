# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Swap the odd and even bits of a positive integer with as few operations as possible.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the input is always a positive int?
  - Yes
- Can we assume we're working with 32 bits?
  - Yes
- Is the output an int?
  - Yes
- Can we assume the inputs are valid (not None)?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- 0 -> 0
- -1 -> -1
- General case

````txt
    input  = 0000 1001 1111 0110
    result = 0000 0110 1111 1001
```txt

## Algorithm

```txt
* Isolate the odd bits with a mask:
    0000 1001 1111 0110  num
    1010 1010 1010 1010  mask
    --------------------------------
    0000 1000 1010 0010  num & mask

* Shift the odd bits right:
    0000 0100 0101 0001  odd

* Isolate the even bits with a mask:
    0000 1001 1111 0110  num
    0101 0101 0101 0101  mask
    --------------------------------
    0000 0001 0101 0100  num & mask

* Shift the even bits left:
    0000 0010 1010 1000  even

* Return even | odd
    0000 0100 0101 0001  odd
    0000 0010 1010 1000  even
    --------------------------------
    0000 0110 1111 1001  odd | even
````

Complexity:

- Time: O(b), where b is the number of bits
- Space: O(b), where b is the number of bits

## Code

```python
class Bits(object):

    def pairwise_swap(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num == 0 or num == 1:
            return num
        odd = (num & int('1010101010101010', base=2)) >> 1
        even = (num & int('0101010101010101', base=2)) << 1
        return odd | even
```

## Unit Test

```python
%%writefile test_pairwise_swap.py
import unittest


class TestBits(unittest.TestCase):

    def test_pairwise_swap(self):
        bits = Bits()
        self.assertEqual(bits.pairwise_swap(0), 0)
        self.assertEqual(bits.pairwise_swap(1), 1)
        num = int('0000100111110110', base=2)
        expected = int('0000011011111001', base=2)
        self.assertEqual(bits.pairwise_swap(num), expected)
        self.assertRaises(TypeError, bits.pairwise_swap, None)

        print('Success: test_pairwise_swap')


def main():
    test = TestBits()
    test.test_pairwise_swap()


if __name__ == '__main__':
    main()
```

    Overwriting test_pairwise_swap.py

```python
%run -i test_pairwise_swap.py
```

    Success: test_pairwise_swap
