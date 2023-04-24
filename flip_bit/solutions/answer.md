This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Flip one bit from 0 to 1 to maximize the longest sequence of 1s.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is the input an int, base 2?
  - Yes
- Can we assume the input is a 32 bit number?
  - Yes
- Do we have to validate the length of the input?
  - No
- Is the output an int?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume we are using a positive number since Python doesn't have an >>> operator?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- All 1's -> Count of 1s
- All 0's -> 1
- General case
  - Trailing zeroes
    - 0000 1111 1101 1101 1111 0011 1111 0000 -> 10 (ten)
  - Trailing ones
    - 0000 1001 1101 1101 1111 0001 1111 0111 -> 9

## Algorithm

- seen = []
- Build a list of sequence counts
  - Look for 0's
    - This will be 0 length if the input has trailing ones
    - Add sequence length to seen
  - Look for 1's
    - Add sequence length to seen
- Find the largest sequence of ones looking at seen
  - Loop through seen
    - On each iteration of the loop, flip what we are looking for from 0 to 1 and vice versa
    - If seen[i] represents 1's, continue, we only want to process 0's
    - If this is our first iteration:
      - max_result = seen[i+1] + 1 if seen[i] > 0
      - continue
    - If we are looking at leading zeroes (i == len(seen)-1):
      - result = seen[i-1] + 1
    - If we are looking at one zero:
      - result = seen[i+1] + seen[i-1] + 1
    - If we are looking at multiple zeroes:
      - result = max(seen[i+1], seen[i-1]) + 1
    - Update max_result based on result

We should make a note that Python does not have a logical right shift operator built in. We can either use a positive number or implement one for a 32 bit number:

    num % 0x100000000 >> n

Complexity:

- Time: O(b)
- Space: O(b)

## Code

```python
class Bits(object):

    MAX_BITS = 32

    def _build_seen_list(self, num):
        seen = []
        looking_for = 0
        count = 0
        for _ in range(self.MAX_BITS):
            if num & 1 != looking_for:
                seen.append(count)
                looking_for = not looking_for
                count = 0
            count += 1
            num >>= 1
        seen.append(count)
        return seen

    def flip_bit(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num == -1:
            return self.MAX_BITS
        if num == 0:
            return 1
        seen = self._build_seen_list(num)
        max_result = 0
        looking_for = 0
        for index, count in enumerate(seen):
            result = 0
            # Only look for zeroes
            if looking_for == 1:
                looking_for = not looking_for
                continue
            # First iteration, take trailing zeroes
            # or trailing ones into account
            if index == 0:
                if count != 0:
                    # Trailing zeroes
                    try:
                        result = seen[index + 1] + 1
                    except IndexError:
                        result = 1
            # Last iteration
            elif index == len(seen) - 1:
                result = 1 + seen[index - 1]
            else:
                # One zero
                if count == 1:
                    result = seen[index + 1] + seen[index - 1] + 1
                # Multiple zeroes
                else:
                    result = max(seen[index + 1], seen[index - 1]) + 1
            if result > max_result:
                max_result = result
            looking_for = not looking_for
        return max_result
```

## Unit Test

```python
%%writefile test_flip_bit.py
import unittest


class TestBits(unittest.TestCase):

    def test_flip_bit(self):
        bits = Bits()
        self.assertRaises(TypeError, bits.flip_bit, None)
        self.assertEqual(bits.flip_bit(0), 1)
        self.assertEqual(bits.flip_bit(-1), bits.MAX_BITS)
        num = int('00001111110111011110001111110000', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00000100111011101111100011111011', base=2)
        expected = 9
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00010011101110111110001111101111', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_flip_bit()


if __name__ == '__main__':
    main()
```

    Overwriting test_flip_bit.py

```python
%run -i test_flip_bit.py
```

    Success: test_print_binary
