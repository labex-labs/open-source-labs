# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Return all subsets of a set.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Should the resulting subsets be unique?
  - Yes, treat 'ab' and 'bc' as the same
- Is the empty set included as a subset?
  - Yes
- Are the inputs unique?
  - No
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None -> None
* '' -> ['']
* 'a' -> ['a', '']
* 'ab' -> ['a', 'ab', 'b', '']
* 'abc' -> ['a', 'ab', 'abc', 'ac',
            'b', 'bc', 'c', '']
* 'aabc' -> ['a', 'aa', 'aab', 'aabc',
             'aac', 'ab', 'abc', 'ac',
             'b', 'bc', 'c', '']
```

## Algorithm

- Build a dictionary of {chars: counts} where counts is the number of times each char is found in the input
- Loop through each item in the dictionary
  - Keep track of the current index (first item will have current index 0)
  - If the char's count is 0, continue
  - Decrement the current char's count in the dictionary
  - Add the current char to the current results
  - Add the current result to the results
  - Recurse, passing in the current index as the new starting point index
    - When we recurse, we'll check if current index < starting point index, and if so, continue
    - This avoids duplicate results such as 'ab' and 'bc'
  - Backtrack by:
    - Removing the just added current char from the current results
    - Incrementing the current char's count in the dictionary

Complexity:

- Time: O(2^n)
- Space: O(2^n) if we are saving each result, or O(n) if we are just printing each result

We are doubling the number of operations every time we add an element to the results: O(2^n).

Note, you could also use the following method to solve this problem:

```txt
number binary  subset
0      000      {}
1      001      {c}
2      010      {b}
3      011      {b,c}
4      100      {a}
5      101      {a,c}
6      110      {a,b}
7      111      {a,b,c}
```

## Code

```python
from collections import OrderedDict


class Combinatoric(object):

    def _build_counts_map(self, string):
        counts_map = OrderedDict()
        for char in string:
            if char in counts_map:
                counts_map[char] += 1
            else:
                counts_map[char] = 1
        return counts_map

    def find_power_set(self, string):
        if string is None:
            return string
        if string == '':
            return ['']
        counts_map = self._build_counts_map(string)
        curr_results = []
        results = []
        self._find_power_set(counts_map, curr_results,
                             results, index=0)
        results.append('')
        return results

    def _find_power_set(self, counts_map, curr_result,
                        results, index):
        for curr_index, char in enumerate(counts_map):
            if curr_index < index or counts_map[char] == 0:
                continue
            curr_result.append(char)
            counts_map[char] -= 1
            results.append(''.join(curr_result))
            self._find_power_set(counts_map, curr_result,
                                 results, curr_index)
            counts_map[char] += 1
            curr_result.pop()
```

## Unit Test

```python
%%writefile test_power_set.py
import unittest


class TestPowerSet(unittest.TestCase):

    def test_power_set(self):
        input_set = ''
        expected = ['']
        self.run_test(input_set, expected)
        input_set = 'a'
        expected = ['a', '']
        self.run_test(input_set, expected)
        input_set = 'ab'
        expected = ['a', 'ab', 'b', '']
        self.run_test(input_set, expected)
        input_set = 'abc'
        expected = ['a', 'ab', 'abc', 'ac',
                    'b', 'bc', 'c', '']
        self.run_test(input_set, expected)
        input_set = 'aabc'
        expected = ['a', 'aa', 'aab', 'aabc',
                    'aac', 'ab', 'abc', 'ac',
                    'b', 'bc', 'c', '']
        self.run_test(input_set, expected)
        print('Success: test_power_set')

    def run_test(self, input_set, expected):
        combinatoric = Combinatoric()
        result = combinatoric.find_power_set(input_set)
        self.assertEqual(result, expected)


def main():
    test = TestPowerSet()
    test.test_power_set()


if __name__ == '__main__':
    main()
```

    Overwriting test_power_set.py

```python
%run -i test_power_set.py
```

    Success: test_power_set
