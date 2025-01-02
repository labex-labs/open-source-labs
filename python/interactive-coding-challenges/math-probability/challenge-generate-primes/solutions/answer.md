# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Generate a list of primes.

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
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]

## Algorithm

For a number to be prime, it must be 2 or greater and cannot be divisible by another number other than itself (and 1).

We'll use the Sieve of Eratosthenes. All non-prime numbers are divisible by a prime number.

- Use an array (or bit array, bit vector) to keep track of each integer up to the max
- Start at 2, end at sqrt(max)
  - We can use sqrt(max) instead of max because:
    - For each value that divides the input number evenly, there is a complement b where a \* b = n
    - If a > sqrt(n) then b < sqrt(n) because sqrt(n^2) = n
  - "Cross off" all numbers divisible by 2, 3, 5, 7, ... by setting array[index] to False

Complexity:

- Time: O(n log log n)
- Space: O(n)

Wikipedia's animation:

![Sieve of Eratosthenes animation](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)

## Code

```python
import math


class PrimeGenerator(object):

    def generate_primes(self, max_num):
        if max_num is None:
            raise TypeError('max_num cannot be None')
        array = [True] * max_num
        array[0] = False
        array[1] = False
        prime = 2
        while prime <= math.sqrt(max_num):
            self._cross_off(array, prime)
            prime = self._next_prime(array, prime)
        return array

    def _cross_off(self, array, prime):
        for index in range(prime*prime, len(array), prime):
            # Start with prime*prime because if we have a k*prime
            # where k < prime, this value would have already been
            # previously crossed off
            array[index] = False

    def _next_prime(self, array, prime):
        next = prime + 1
        while next < len(array) and not array[next]:
            next += 1
        return next
```

## Unit Test

```python
%%writefile test_generate_primes.py
import unittest


class TestMath(unittest.TestCase):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        self.assertRaises(TypeError, prime_generator.generate_primes, None)
        self.assertRaises(TypeError, prime_generator.generate_primes, 98.6)
        self.assertEqual(prime_generator.generate_primes(20), [False, False, True,
                                                           True, False, True,
                                                           False, True, False,
                                                           False, False, True,
                                                           False, True, False,
                                                           False, False, True,
                                                           False, True])
        print('Success: generate_primes')


def main():
    test = TestMath()
    test.test_generate_primes()


if __name__ == '__main__':
    main()
```

    Overwriting test_generate_primes.py

```python
%run -i test_generate_primes.py
```

    Success: generate_primes
