# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: You are running up n steps. If you can take a single, double, or triple step, how many possible ways are there to run up to the nth step?

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- If n == 0, what should the result be?
  - Go with 1, but discuss different approaches
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None or negative input -> Exception
- n == 0 -> 1
- n == 1 -> 1
- n == 2 -> 2
- n == 3 -> 4
- n == 4 -> 7
- n == 10 -> 274

## Algorithm

To get to step n, we will need to have gone:

- One step from n-1
- Two steps from n-2
- Three steps from n-3

If we go the one step route above, we'll be at n-1 before taking the last step. To get to step n-1, we will need to have gone:

- One step from n-1-1
- Two steps from n-1-2
- Three steps from n-1-2

Continue this process until we reach the start.

Base case:

- If n < 0: return 0
- If n == 0: return 1

Note, if we had chosen n == 0 to return 0 instead, we would need to add additional base cases. Otherwise we'd be adding multiple 0's once we hit the base cases and not get any result > 0.

Recursive case:

We'll memoize the solution to improve performance.

- Use the memo if we've already processed the current step.
- Update the memo by adding the recursive calls to step(n-1), step(n-2), step(n-3)

Complexity:

- Time: O(n), if using memoization
- Space: O(n), where n is the recursion depth

Note: The number of ways will quickly overflow the bounds of an integer.

## Code

```python
class Steps(object):

    def count_ways(self, num_steps):
        if num_steps is None or num_steps < 0:
            raise TypeError('num_steps cannot be None or negative')
        cache = {}
        return self._count_ways(num_steps, cache)

    def _count_ways(self, num_steps, cache):
        if num_steps < 0:
            return 0
        if num_steps == 0:
            return 1
        if num_steps in cache:
            return cache[num_steps]
        cache[num_steps] = (self._count_ways(num_steps-1, cache) +
                            self._count_ways(num_steps-2, cache) +
                            self._count_ways(num_steps-3, cache))
        return cache[num_steps]
```

## Unit Test

```python
%%writefile test_steps.py
import unittest


class TestSteps(unittest.TestCase):

    def test_steps(self):
        steps = Steps()
        self.assertRaises(TypeError, steps.count_ways, None)
        self.assertRaises(TypeError, steps.count_ways, -1)
        self.assertEqual(steps.count_ways(0), 1)
        self.assertEqual(steps.count_ways(1), 1)
        self.assertEqual(steps.count_ways(2), 2)
        self.assertEqual(steps.count_ways(3), 4)
        self.assertEqual(steps.count_ways(4), 7)
        self.assertEqual(steps.count_ways(10), 274)
        print('Success: test_steps')


def main():
    test = TestSteps()
    test.test_steps()


if __name__ == '__main__':
    main()
```

    Overwriting test_steps.py

```python
%run -i test_steps.py
```

    Success: test_steps
