This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement radix sort.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is the input a list?
  - Yes
- Can we assume the inputs are valid?
  - Check for None in place of an array
  - Assume array elements are ints
- Do we know the max digits to handle?
  - No
- Are the digits base 10?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- [] -> []
- [128, 256, 164, 8, 2, 148, 212, 242, 244] -> [2, 8, 128, 148, 164, 212, 242, 244, 256]

## Algorithm

Sample input: [1, 220, 122, 112]

- We'll evaluate each digit starting with the ones position
  - [**1**, 22**0**, 12**2**, 11**2**]
    - Bucket 0: 220
    - Bucket 1: 1
    - Bucket 2: 122, 112
    - Result: [220, 1, 122, 112]
  - [2**2**0, 1, 1**2**2, 1**1**2]
    - Bucket 0: 1
    - Bucket 1: 112
    - Bucket 2: 220, 122
    - Result: [1, 112, 220, 122]
  - [1, **1**12, **2**20, **1**22]
    - Bucket 0: 1
    - Bucket 1: 112, 122
    - Bucket 2: 220
    - Result: [1, 112, 122, 220]

Bucketing example: 123

- Ones
  - 12**3** // 10^0 = 123
  - 123 % 10 = 3
- Tens
  - 1**2**3 // 10^1 = 12
  - 12 % 10 = 2
- Hundreds
  - **1**23 // 10^2 = 1
  - 1 % 10 = 1

Complexity:

- Time: O(k\*n), where n is the number of items and k is the number of digits in the largest item
- Space: O(k+n)

Misc:

- Not in-place
- Most implementations are stable

If k (the number of digits) is less than log(n), radix sort can be faster than algorithms such as quicksort.

## Code

```python
class RadixSort(object):

    def sort(self, array, base=10):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return []
        max_element = max(array)
        max_digits = len(str(abs(max_element)))
        curr_array = array
        for digit in range(max_digits):
            buckets = [[] for _ in range(base)]
            for item in curr_array:
                buckets[(item//(base**digit))%base].append(item)
            curr_array = []
            for bucket in buckets:
                curr_array.extend(bucket)
        return curr_array
```

## Unit Test

```python
%%writefile test_radix_sort.py
import unittest


class TestRadixSort(unittest.TestCase):

    def test_sort(self):
        radix_sort = RadixSort()
        self.assertRaises(TypeError, radix_sort.sort, None)
        self.assertEqual(radix_sort.sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        self.assertEqual(radix_sort.sort(array), expected)
        print('Success: test_sort')


def main():
    test = TestRadixSort()
    test.test_sort()


if __name__ == '__main__':
    main()
```

    Overwriting test_radix_sort.py

```python
%run -i test_radix_sort.py
```

    Success: test_sort
