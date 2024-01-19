# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Given an int, repeatedly add its digits until the result is one digit.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume num is not negative?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None input -> TypeError
* negative input -> ValueError
* 9 -> 9
* 138 -> 3
* 65536 -> 7
```

## Algorithm

The naive solution simply isolates each digit with with modulo and integer division. We'll add each isolated digit to a list and sum the values.

```txt
138 % 10 = 8 -> isolated
138 // 10 = 13
13 % 10 = 3 -> isolated
13 // 10 = 1
1 % 10 = 1 -> isolated
```

A more optimal solution exists, by recognizing this is a digital root. See the [Wikipedia article](https://en.wikipedia.org/wiki/Digital_root) for more information.

Complexity:

- Time: O(1)
- Space: O(1)

## Code

```python
class Solution(object):

    def add_digits(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 0:
            raise ValueError('num cannot be negative')
        digits = []
        while num != 0:
            digits.append(num % 10)
            num //= 10
        digits_sum = sum(digits)
        if digits_sum >= 10:
            return self.add_digits(digits_sum)
        else:
            return digits_sum

    def add_digits_optimized(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 0:
            raise ValueError('num cannot be negative')
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
```

## Unit Test

```python
%%writefile test_add_digits.py
import unittest


class TestAddDigits(unittest.TestCase):

    def test_add_digits(self, func):
        self.assertRaises(TypeError, func, None)
        self.assertRaises(ValueError, func, -1)
        self.assertEqual(func(0), 0)
        self.assertEqual(func(9), 9)
        self.assertEqual(func(138), 3)
        self.assertEqual(func(65536), 7)
        print('Success: test_add_digits')


def main():
    test = TestAddDigits()
    solution = Solution()
    test.test_add_digits(solution.add_digits)
    try:
        test.test_add_digits(solution.add_digits_optimized)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
```

    Overwriting test_add_digits.py

```python
%run -i test_add_digits.py
```

    Success: test_add_digits
    Success: test_add_digits
