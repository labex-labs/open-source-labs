# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Move all zeroes in a list to the end.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is the input an array of ints?
  - Yes
- Is the output a new array of ints?
  - No, do this in-place
- Do we need to maintain ordering of non-zero values?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None -> TypeError
* [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
* [1, 0] -> [1, 0]
* [0, 1] -> [1, 0]
* [0] -> [0]
* [1] -> [1]
* [1, 1] -> [1, 1]
```

## Algorithm

- pos = 0
- Loop through each item in the input
  - If the item != 0, set input[pos] = item
    - pos++
- Fill input[pos:] with zeroes

```txt
 |
[0, 1, 0, 3, 12]
 ^
    |
[0, 1, 0, 3, 12]
 ^
    |
[1, 1, 0, 3, 12]
 ^
       |
[1, 1, 0, 3, 12]
    ^
          |
[1, 1, 0, 3, 12]
    ^
          |
[1, 3, 0, 3, 12]
    ^
              |
[1, 3, 0, 3, 12]
       ^
              |
[1, 3, 12, 3, 12]
       ^

Fill right with zeroes:

[1, 3, 12, 3, 12]
           ^
[1, 3, 12, 0, 12]
           ^
[1, 3, 12, 0, 0]
              ^
```

Complexity:

- Time: O(n)
- Space: O(1)

## Code

```python
class Solution(object):

    def move_zeroes(self, nums):
        if nums is None:
            raise TypeError('nums cannot be None')
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        if pos < len(nums):
            nums[pos:] = [0] * (len(nums) - pos)
```

## Unit Test

```python
%%writefile test_move_zeroes.py
import unittest


class TestMoveZeroes(unittest.TestCase):

    def test_move_zeroes(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.move_zeroes, None)
        array = [0, 1, 0, 3, 12]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 3, 12, 0, 0])
        array = [1, 0]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0]
        solution.move_zeroes(array)
        self.assertEqual(array, [0])
        array = [1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1])
        array = [1, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 1])
        print('Success: test_move_zeroes')


def main():
    test = TestMoveZeroes()
    test.test_move_zeroes()


if __name__ == '__main__':
    main()
```

    Overwriting test_move_zeroes.py

```python
%run -i test_move_zeroes.py
```

    Success: test_move_zeroes
