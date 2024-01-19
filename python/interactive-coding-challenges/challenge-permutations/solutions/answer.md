# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find all permutations of an input string.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can the input have duplicates?
  - Yes
- Can the output have duplicates?
  - No
- Is the output a list of strings?
  - Yes
- Do we have to output the results in sorted order?
  - No
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None -> None
* '' -> ''
* 'AABC' -> ['AABC', 'AACB', 'ABAC', 'ABCA',
             'ACAB', 'ACBA', 'BAAC', 'BACA',
             'BCAA', 'CAAB', 'CABA', 'CBAA']
```

## Algorithm

- Build a dictionary of {chars: counts} where counts is the number of times each char is found in the input
- Loop through each item in the dictionary
  - If the counts is 0, continue
  - Decrement the current char's count in the dictionary
  - Add the current char to the current results
  - If the current result is the same length as the input, add it to the results
  - Else, recurse
  - Backtrack by:
    - Removing the just added current char from the current results
    - Incrementing the current char's count in the dictionary

Complexity:

- Time: O(n!)
- Space: O(n!) since we are storing the results in an array, or O(n) if we are just printing each result

## Code

```python
from collections import OrderedDict


class Permutations(object):

    def _build_counts_map(self, string):
        counts_map = OrderedDict()
        for char in string:
            if char in counts_map:
                counts_map[char] += 1
            else:
                counts_map[char] = 1
        return counts_map

    def find_permutations(self, string):
        if string is None or string == '':
            return string
        counts_map = self._build_counts_map(string)
        curr_results = []
        results = []
        self._find_permutations(counts_map, curr_results, results, len(string))
        return results

    def _find_permutations(self, counts_map, curr_result,
                           results, input_length):
        for char in counts_map:
            if counts_map[char] == 0:
                continue
            curr_result.append(char)
            counts_map[char] -= 1
            if len(curr_result) == input_length:
                results.append(''.join(curr_result))
            else:
                self._find_permutations(counts_map, curr_result,
                                        results, input_length)
            counts_map[char] += 1
            curr_result.pop()
```

## Unit Test

```python
%%writefile test_permutations.py
import unittest


class TestPermutations(unittest.TestCase):

    def test_permutations(self):
        permutations = Permutations()
        self.assertEqual(permutations.find_permutations(None), None)
        self.assertEqual(permutations.find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        self.assertEqual(permutations.find_permutations(string), expected)
        print('Success: test_permutations')


def main():
    test = TestPermutations()
    test.test_permutations()


if __name__ == '__main__':
    main()
```

    Overwriting test_permutations.py

```python
%run -i test_permutations.py
```

    Success: test_permutations
