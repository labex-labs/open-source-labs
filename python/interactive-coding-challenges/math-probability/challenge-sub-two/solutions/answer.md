# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find the difference of two integers without using the + or - sign.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the inputs are valid?
  - No, check for None
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None input -> TypeError
* 7, 5 -> 2
* -5, -7 -> 2
* -5, 7 -> -12
* 5, -7 -> 12
```

## Algorithm

We'll look at the following example, subtracting a and b:

```txt
a 0110 = 6
b 0101 = 5
```

First, subtract a and b, without worrying about the borrow (0-0=0, 0-1=1, 1-1=0):

result = a ^ b = 0011

Next, calculate the borrow (0-1=1). We'll need to left shift one to prepare for the next iteration when we move to the next most significant bit:

~a = 1001
b = 0101
~a & b = 0001

borrow = (~a&b) << 1 = 0010

If the borrow is not zero, we'll need to subtract the borrow from the result. Recursively call the function, passing in result and borrow.

Complexity:

- Time: O(b), where b is the number of bits
- Space: O(b), where b is the number of bits

## Code

```python
class Solution(object):

    def sub_two(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b;
        borrow = (~a & b) << 1
        if borrow != 0:
            return self.sub_two(result, borrow)
        return result;
```

## Unit Test

```python
%%writefile test_sub_two.py
import unittest


class TestSubTwo(unittest.TestCase):

    def test_sub_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.sub_two, None)
        self.assertEqual(solution.sub_two(7, 5), 2)
        self.assertEqual(solution.sub_two(-5, -7), 2)
        self.assertEqual(solution.sub_two(-5, 7), -12)
        self.assertEqual(solution.sub_two(5, -7), 12)
        print('Success: test_sub_two')


def main():
    test = TestSubTwo()
    test.test_sub_two()


if __name__ == '__main__':
    main()
```

    Overwriting test_sub_two.py

```python
%run -i test_sub_two.py
```

    Success: test_sub_two
