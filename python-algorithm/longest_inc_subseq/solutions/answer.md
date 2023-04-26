This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Find the longest increasing subsequence.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Are duplicates possible?
  - Yes
- Can we assume the inputs are integers?
  - Yes
- Can we assume the inputs are valid?
  - No
- Do we expect the result to be an array of the longest increasing subsequence?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- [] -> []
- [3, 4, -1, 0, 6, 2, 3] -> [-1, 0, 2, 3]

## Algorithm

We'll use bottom up dynamic programming to build a table.

```txt
Init a temp array of size len(input) to 1.
We'll use l and r to iterate through the input.
Array prev will hold the index of the prior smaller value, used to reconstruct the final sequence.

if input[l] < input[r]:
    if temp[r] < temp[l] + 1:
        temp[r] = temp[l] + 1
        prev[r] = l

        l  r
index:  0  1  2  3  4  5  6
---------------------------
input:  3  4 -1  0  6  2  3
temp:   1  2  1  1  1  1  1
prev:   x  x  x  x  x  x  x

End result:

index:  0  1  2  3  4  5  6
---------------------------
input:  3  4 -1  0  6  2  3
temp:   1  2  1  2  3  3  4
prev:   x  0  x  2  1  3  5
```

Complexity:

- Time: O(n^2)
- Space: O(n)

## Code

```python
class Subsequence(object):

    def longest_inc_subseq(self, seq):
        if seq is None:
            raise TypeError('seq cannot be None')
        if not seq:
            return []
        temp = [1] * len(seq)
        prev = [None] * len(seq)
        for r in range(1, len(seq)):
            for l in range(r):
                if seq[l] < seq[r]:
                    if temp[r] < temp[l] + 1:
                        temp[r] = temp[l] + 1
                        prev[r] = l
        max_val = 0
        max_index = -1
        results = []
        for index, value in enumerate(temp):
            if value > max_val:
                max_val = value
                max_index = index
        curr_index = max_index
        while curr_index is not None:
            results.append(seq[curr_index])
            curr_index = prev[curr_index]
        return results[::-1]
```

## Unit Test

```python
%%writefile test_longest_increasing_subseq.py
import unittest


class TestLongestIncreasingSubseq(unittest.TestCase):

    def test_longest_increasing_subseq(self):
        subseq = Subsequence()
        self.assertRaises(TypeError, subseq.longest_inc_subseq, None)
        self.assertEqual(subseq.longest_inc_subseq([]), [])
        seq = [3, 4, -1, 0, 6, 2, 3]
        expected = [-1, 0, 2, 3]
        self.assertEqual(subseq.longest_inc_subseq(seq), expected)
        print('Success: test_longest_increasing_subseq')


def main():
    test = TestLongestIncreasingSubseq()
    test.test_longest_increasing_subseq()


if __name__ == '__main__':
    main()
```

    Overwriting test_longest_increasing_subseq.py

```python
%run -i test_longest_increasing_subseq.py
```

    Success: test_longest_increasing_subseq
