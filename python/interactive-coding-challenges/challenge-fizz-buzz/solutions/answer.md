# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement Fizz Buzz.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- What is fizz buzz?
  - Return the string representation of numbers from 1 to n
    - Multiples of 3 -> 'Fizz'
    - Multiples of 5 -> 'Buzz'
    - Multiples of 3 and 5 -> 'FizzBuzz'
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None -> Exception
* < 1 -> Exception
* 15 ->
[
    '1',
    '2',
    'Fizz',
    '4',
    'Buzz',
    'Fizz',
    '7',
    '8',
    'Fizz',
    'Buzz',
    '11',
    'Fizz',
    '13',
    '14',
    'FizzBuzz'
]
```

## Algorithm

There is no fancy algorithm to solve fizz buzz.

- Iterate from 1 through n
- Use the mod operator to determine if the current iteration is divisible by:
  - 3 and 5 -> 'FizzBuzz'
  - 3 -> 'Fizz'
  - 5 -> 'Buzz'
  - else -> string of current iteration
- return the results

Complexity:

- Time: O(n)
- Space: O(n)

## Code

```python
class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 1:
            raise ValueError('num cannot be less than one')
        results = []
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results
```

## Unit Test

```python
%%writefile test_fizz_buzz.py
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.fizz_buzz, None)
        self.assertRaises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()
```

    Overwriting test_fizz_buzz.py

```python
%run -i test_fizz_buzz.py
```

    Success: test_fizz_buzz

```python

```
