# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find the length of the longest substring with at most k distinct characters.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the inputs are valid?
  - No
- Can we assume the strings are ASCII?
  - Yes
- Is this case sensitive?
  - Yes
- Is a substring a contiguous block of chars?
  - Yes
- Do we expect an int as a result?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> TypeError
- '', k = 3 -> 0
- 'abcabcdefgghiij', k=3 -> 6
- 'abcabcdefgghighij', k=3 -> 7

## Algorithm

We'll use a `chars_to_index_map` dictionary: char (key) to index (val) map to maintain a sliding window.

The index (val) will keep track of the character index in the input string.

For each character in the string:

- Add the char (key) and index (value) to the map
- If the length of our map is greater than k, then we'll need to eliminate one item
  - Scan the map to find the lowest index and remove it
  - The new lowest index will therefore be incremented by 1
- The max length will be the current index minus the lower index + 1

Complexity:

- Time: O(n \* k), where n is the number of chars, k is the length of the map due to the min() call
- Space: O(n)

## Code

```python
class Solution(object):

    def longest_substr(self, string, k):
        if string is None:
            raise TypeError('string cannot be None')
        if k is None:
            raise TypeError('k cannot be None')
        low_index = 0
        max_length = 0
        chars_to_index_map = {}
        for index, char in enumerate(string):
            chars_to_index_map[char] = index
            if len(chars_to_index_map) > k:
                low_index = min(chars_to_index_map.values())
                del chars_to_index_map[string[low_index]]
                low_index += 1
            max_length = max(max_length, index - low_index + 1)
        return max_length
```

## Unit Test

```python
%%writefile test_longest_substr.py
import unittest


class TestSolution(unittest.TestCase):

    def test_longest_substr(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.longest_substr, None)
        self.assertEqual(solution.longest_substr('', k=3), 0)
        self.assertEqual(solution.longest_substr('abcabcdefgghiij', k=3), 6)
        self.assertEqual(solution.longest_substr('abcabcdefgghighij', k=3), 7)
        print('Success: test_longest_substr')


def main():
    test = TestSolution()
    test.test_longest_substr()


if __name__ == '__main__':
    main()
```

    Overwriting test_longest_substr.py

```python
%run -i test_longest_substr.py
```

    Success: test_longest_substr
