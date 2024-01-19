# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Check if a number is prime.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is it correct that 1 is not considered a prime number?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- Not an int -> Exception
- Less than 2 -> False
- General case

## Algorithm

For a number to be prime, it must be 2 or greater and cannot be divisible by another number other than itself (and 1).

We'll check by dividing all numbers from 2 to the input number to determine if the number is prime.

As an optimization, we can divide from 2 to the square root of the input number. For each value that divides the input number evenly, there is a complement b where a \* b = n. If a > sqrt(n) then b < sqrt(n) because sqrt(n^2) = n.

Complexity:

- Time: O(n) where n is the value of the input number
- Space: O(1)

### Sieve of Eratosthenes

The Sieve of Eratosthenes provides a more efficient way of computing and generating primes. See the challenge ["Generate a list of primes"]() for more details.

## Code

```python
import math


class Math(object):

    def check_prime(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def check_prime_optimized(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True
```

## Unit Test

```python
%%writefile test_check_prime.py
import unittest


class TestMath(unittest.TestCase):

    def test_check_prime(self):
        math = Math()
        self.assertRaises(TypeError, math.check_prime, None)
        self.assertRaises(TypeError, math.check_prime, 98.6)
        self.assertEqual(math.check_prime(0), False)
        self.assertEqual(math.check_prime(1), False)
        self.assertEqual(math.check_prime(97), True)
        print('Success: test_check_prime')


def main():
    test = TestMath()
    test.test_check_prime()


if __name__ == '__main__':
    main()
```

    Overwriting test_check_prime.py

```python
%run -i test_check_prime.py
```

    Success: test_check_prime
