# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Given a list of ints, find the products of every other int for each index.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we use division?
  - No
- Is the output a list of ints?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None -> TypeError
* [] -> []
* [0] -> []
* [0, 1] -> [1, 0]
* [0, 1, 2] -> [2, 0, 0]
* [1, 2, 3, 4] -> [24, 12, 8, 6]
```

## Algorithm

### Brute force:

```txt
sum = 1
 |
[1, 2, 3, 4]
 ^
skip if both pointers are pointing to the same spot
    |
[1, 2, 3, 4]
 ^
sum *= 2
       |
[1, 2, 3, 4]
 ^
sum *= 3
          |
[1, 2, 3, 4]
 ^
sum *= 4
results.append(sum)
results = [24]

repeat for every element in the input list to obtain:

[24, 12, 8, 6]

```

Complexity:

- Time: O(n^2)
- Space: O(n)

### Greedy

```txt
input  = [1, 2, 3, 4]
result = [2*3*4, 1*3*4, 1*2*4, 1*2*3]

Note we are duplicating multiplications with the brute force approach.

We'll calculate all products before an index, and all products after an index.
We'll then multiple these two together to form the result.

input  = [1,         2,     3,     4]
before = [1,         1,   1*2, 1*2*3]
after  = [2*3*4, 1*3*4, 1*2*4,     1]
result = [   24,    12,     8,     6]
```

Complexity:

- Time: O(n)
- Space: O(n)

## Code

```python
class Solution(object):

    def mult_other_numbers_brute(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return array
        if len(array) == 1:
            return []
        result = []
        for i in range(len(array)):
            curr_sum = 1
            for j in range(len(array)):
                if i == j:
                    continue
                curr_sum *= array[j]
            result.append(curr_sum)
        return result

    def mult_other_numbers(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return array
        if len(array) == 1:
            return []
        result = [None] * len(array)
        curr_product = 1
        for i in range(len(array)):
            result[i] = curr_product
            curr_product *= array[i]
        curr_product = 1
        for i in range(len(array))[::-1]:
            result[i] *= curr_product
            curr_product *= array[i]
        return result
```

## Unit Test

```python
%%writefile test_mult_other_numbers.py
import unittest


class TestMultOtherNumbers(unittest.TestCase):

    def test_mult_other_numbers(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.mult_other_numbers, None)
        self.assertEqual(solution.mult_other_numbers([0]), [])
        self.assertEqual(solution.mult_other_numbers([0, 1]), [1, 0])
        self.assertEqual(solution.mult_other_numbers([0, 1, 2]), [2, 0, 0])
        self.assertEqual(solution.mult_other_numbers([1, 2, 3, 4]), [24, 12, 8, 6])
        print('Success: test_mult_other_numbers')


def main():
    test = TestMultOtherNumbers()
    test.test_mult_other_numbers()


if __name__ == '__main__':
    main()
```

    Overwriting test_mult_other_numbers.py

```python
%run -i test_mult_other_numbers.py
```

    Success: test_mult_other_numbers
