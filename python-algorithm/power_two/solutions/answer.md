This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Determine if a number is a power of two.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is the input number an int?
  - Yes
- Can we assume the inputs are valid?
  - No
- Is the output a boolean?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> TypeError
- 0 -> False
- 1 -> True
- 2 -> True
- 15 -> False
- 16 -> True

## Algorithm

We can use bit manipulation to determine if a number is a power of two.

For a number to be a power of two, there must only be one bit that is a `1`.

We can use the following bit manipulation trick to determine this:

`n & (n - 1)`

Here's an example why:

```txt
0000 1000 = n
0000 0001 = 1
0000 0111 = n-1

0000 1000 = n
0000 0111 = n-1
0000 0000 = n & n-1, result = 0
```

Complexity:

- Time: O(1)
- Space: O(1)

## Code

```python
class Solution(object):

    def is_power_of_two(self, n):
        if n is None:
            raise TypeError('n cannot be None')
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
```

## Unit Test

```python
%%writefile test_is_power_of_two.py
import unittest


class TestSolution(unittest.TestCase):

    def test_is_power_of_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.is_power_of_two, None)
        self.assertEqual(solution.is_power_of_two(0), False)
        self.assertEqual(solution.is_power_of_two(1), True)
        self.assertEqual(solution.is_power_of_two(2), True)
        self.assertEqual(solution.is_power_of_two(15), False)
        self.assertEqual(solution.is_power_of_two(16), True)
        print('Success: test_is_power_of_two')


def main():
    test = TestSolution()
    test.test_is_power_of_two()


if __name__ == '__main__':
    main()
```

    Overwriting test_is_power_of_two.py

```python
%run -i test_is_power_of_two.py
```

    Success: test_is_power_of_two
