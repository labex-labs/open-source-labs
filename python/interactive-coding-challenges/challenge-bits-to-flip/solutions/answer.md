# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Determine the number of bits to flip to convert int a to int b.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume A and B are always ints?
  - Yes
- Is the output an int?
  - Yes
- Can we assume A and B are always the same number of bits?
  - Yes
- Can we assume the inputs are valid (not None)?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- A or B is None -> Exception
- General case

````txt
    A = 11101
    B = 01111
    Result: 2
```txt

## Algorithm

We can use the xor operator to determine the bit differences between a and b

- Set count to 0
- Set c to a xor b
- Loop while c != 0:
  - Increment count if the LSB in c is a 1
    - We can check this by using a mask of 1
  - Right shift c by 1
- Return the count

Complexity:

- Time: O(b), where b is the number of bits
- Space: O(b), where b is the number of bits

## Code

```python
class Bits(object):

    def bits_to_flip(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        count = 0
        c = a ^ b
        while c:
            count += c & 1
            c >>= 1
        return count
````

## Unit Test

```python
%%writefile test_bits_to_flip.py
import unittest


class TestBits(unittest.TestCase):

    def test_bits_to_flip(self):
        bits = Bits()
        a = int('11101', base=2)
        b = int('01111', base=2)
        expected = 2
        self.assertEqual(bits.bits_to_flip(a, b), expected)
        print('Success: test_bits_to_flip')


def main():
    test = TestBits()
    test.test_bits_to_flip()


if __name__ == '__main__':
    main()
```

    Overwriting test_bits_to_flip.py

```python
%run -i test_bits_to_flip.py
```

    Success: test_bits_to_flip
