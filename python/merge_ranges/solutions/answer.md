This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Given a list of tuples representing ranges, condense the ranges.

Example: [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Are the tuples in sorted order?
  - No
- Are the tuples ints?
  - Yes
- Will all tuples have the first element less than the second?
  - Yes
- Is there an upper bound on the input range?
  - No
- Is the output a list of tuples?
  - Yes
- Is the output a new array?
  - Yes
- Can we assume the inputs are valid?
  - No, check for None
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* None input -> TypeError
* [] - []
* [(2, 3), (7, 9)] -> [(2, 3), (7, 9)]
* [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]
* [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)] -> [(1, 11)]
* [(2, 3), (3, 8), (7, 9), (8, 10)] -> [(2, 10)]
```

## Algorithm

- Sort the tuples based on start time
- Check each adjacent tuple to see if they can be merged

```txt
Case: * [(2, 3), (3, 8), (7, 9), (8, 10)] -> [(2, 10)]

* Sort by start time (already sorted)
* Add the first tuple to the merged_array
* Loop through each item in sorted_array starting at index 1
    * If there is no overlap
        * Add the current item to merged_array
    * Else
        * Update the last item in merged_array
            * The end time will be the max of merged_array[-1][1] and sorted_array[i][1]

Start:
                           i
                   0       1       2       3
sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
merged_array = [(2, 3)]

Overlap with (2, 3), (3, 8):
                           i
                   0       1       2       3
sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
merged_array = [(2, 8)]

Overlap with (2, 8), (7, 9):
                                   i
                   0       1       2       3
sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
merged_array = [(2, 9)]

Overlap with (2, 9) (8, 10):
                                   i
                   0       1       2       3
sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
merged_array = [(2, 10)]
```

Complexity:

- Time: O(n log(n))
- Space: O(n)

## Code

```python
class Solution(object):

    def merge_ranges(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return array
        sorted_array = sorted(array)
        merged_array = [sorted_array[0]]
        for index, item in enumerate(sorted_array):
            if index == 0:
                continue
            start_prev, end_prev = merged_array[-1]
            start_curr, end_curr = item
            if end_prev < start_curr:
                # No overlap, add the entry
                merged_array.append(item)
            else:
                # Overlap, update the previous entry's end value
                merged_array[-1] = (start_prev, max(end_prev, end_curr))
        return merged_array
```

## Unit Test

```python
%%writefile test_merge_ranges.py
import unittest


class TestMergeRanges(unittest.TestCase):

    def test_merge_ranges(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.merge_ranges, None)
        self.assertEqual(solution.merge_ranges([]), [])
        array = [(2, 3), (7, 9)]
        expected = [(2, 3), (7, 9)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(3, 5), (2, 3), (7, 9), (8, 10)]
        expected = [(2, 5), (7, 10)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)]
        expected = [(1, 11)]
        self.assertEqual(solution.merge_ranges(array), expected)
        print('Success: test_merge_ranges')


def main():
    test = TestMergeRanges()
    test.test_merge_ranges()


if __name__ == '__main__':
    main()
```

    Overwriting test_merge_ranges.py

```python
%run -i test_merge_ranges.py
```

    Success: test_merge_ranges
