# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Given sorted arrays A, B, merge B into A in sorted order.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Does A have enough space for B?
  - Yes
- Can the inputs have duplicate array items?
  - Yes
- Can we assume the inputs are valid?
  - No
- Does the inputs also include the actual size of A and B?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- A or B is None -> Exception
- index of last A or B < 0 -> Exception
- A or B is empty
- General case
  - A = [1, 3, 5, 7, 9, None, None, None]
  - B = [4, 5, 6]
  - A = [1, 3, 4, 5, 5, 6, 7, 9]

## Algorithm

```txt
                     i                 k
A = [1,  3,  5,  7,  9,  None,  None,  None]
             j
B = [4,  5,  6]

---

A[k] = max(A[i], B[j])
                     i                 k
A = [1,  3,  5,  7,  9,  None,  None,  9]
             j
B = [4,  5,  6]

---

A[k] = max(A[i], B[j])
                 i              k
A = [1,  3,  5,  7,  9,  None,  7,  9]
             j
B = [4,  5,  6]

---

A[k] = max(A[i], B[j])
             i           k
A = [1,  3,  5,  7,  9,  6,  7,  9]
             j
B = [4,  5,  6]

---

A[k] = max(A[i], B[j])
             i       k
A = [1,  3,  5,  7,  5,  6,  7,  9]
         j
B = [4,  5,  6]

---

A[k] = max(A[i], B[j])
         i       k
A = [1,  3,  5,  5,  5,  6,  7,  9]
         j
B = [4,  5,  6]

---

A[k] = max(A[i], B[j])
         i   k
A = [1,  3,  4,  5,  5,  6,  7,  9]
     j
B = [4,  5,  6]

---

A[k] = max(A[i], B[j])
        ik
A = [1,  3,  4,  5,  5,  6,  7,  9]

B = [4,  5,  6]

---

A = [1, 3, 4, 5, 5, 6, 7, 9]

```

Complexity:

- Time: O(m + n)
- Space: O(1)

## Code

```python
class Array(object):

    def merge_into(self, source, dest, source_end_index, dest_end_index):
        if source is None or dest is None:
            raise TypeError('source or dest cannot be None')
        if source_end_index < 0 or dest_end_index < 0:
            raise ValueError('end indices must be >= 0')
        if not source:
            return dest
        if not dest:
            return source
        source_index = source_end_index - 1
        dest_index = dest_end_index - 1
        insert_index = source_end_index + dest_end_index - 1
        while dest_index >= 0:
            if source[source_index] > dest[dest_index]:
                source[insert_index] = source[source_index]
                source_index -= 1
            else:
                source[insert_index] = dest[dest_index]
                dest_index -= 1
            insert_index -= 1
        return source
```

## Unit Test

```python
%%writefile test_merge_into.py
import unittest


class TestArray(unittest.TestCase):

    def test_merge_into(self):
        array = Array()
        self.assertRaises(TypeError, array.merge_into, None, None, None, None)
        self.assertRaises(ValueError, array.merge_into, [1], [2], -1, -1)
        a = [1, 2, 3]
        self.assertEqual(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1, 2, 3]
        self.assertEqual(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1,  3,  5,  7,  9,  None,  None,  None]
        b = [4,  5,  6]
        expected = [1, 3, 4, 5, 5, 6, 7, 9]
        self.assertEqual(array.merge_into(a, b, 5, len(b)), expected)
        print('Success: test_merge_into')


def main():
    test = TestArray()
    test.test_merge_into()


if __name__ == '__main__':
    main()
```

    Overwriting test_merge_into.py

```python
%run -i test_merge_into.py
```

    Success: test_merge_into
