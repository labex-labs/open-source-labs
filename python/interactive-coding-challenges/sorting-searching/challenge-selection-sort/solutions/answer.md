# Solutions

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement selection sort.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is a naive solution sufficient (ie not stable, not based on a heap)?
  - Yes
- Are duplicates allowed?
  - Yes
- Can we assume the input is valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- [] -> []
- One element -> [element]
- Two or more elements

## Algorithm

Wikipedia's animation:
![alt text](http://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)

We can do this recursively or iteratively. Iteratively will be more efficient as it doesn't require the extra space overhead with the recursive calls.

- For each element
  - Check every element to the right to find the min
  - If min < current element, swap

Complexity:

- Time: O(n^2) average, worst, best
- Space: O(1) iterative, O(m) recursive where m is the recursion depth (unless tail-call elimination is available, then O(1))
  - Note: Tail call elimination is not inherently available in Python, see the following [StackOverflow post](http://stackoverflow.com/a/13592002).

Misc:

- In-place
- Most implementations are not stable, due to swapping of values

Selection sort might be a good option if moving elements is more expensive than comparing them, as it requires at most n-1 swaps.

The finding of a minimum element can be done with a min heap, which would change the worst-case run time to O(n log(n)) and increase the space to O(n). This is called a heap sort.

## Code

```python
class SelectionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if data[min_index] < data[i]:
                data[i], data[min_index] = data[min_index], data[i]
        return data

    def sort_iterative_alt(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            self._swap(data, i, self._find_min_index(data, i))
        return data

    def sort_recursive(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        return self._sort_recursive(data, start=0)

    def _sort_recursive(self, data, start):
        if data is None:
            return
        if start < len(data) - 1:
            swap(data, start, self._find_min_index(data, start))
            self._sort_recursive(data, start + 1)
        return data

    def _find_min_index(self, data, start):
        min_index = start
        for i in range(start + 1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        return min_index

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data
```

## Unit Test

```python
%%writefile test_selection_sort.py
import unittest


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self, func):
        print('None input')
        self.assertRaises(TypeError, func, None)

        print('Empty input')
        self.assertEqual(func([]), [])

        print('One element')
        self.assertEqual(func([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        self.assertEqual(func(data), sorted(data))

        print('Success: test_selection_sort\n')


def main():
    test = TestSelectionSort()
    selection_sort = SelectionSort()
    test.test_selection_sort(selection_sort.sort)
    try:
        test.test_selection_sort(selection_sort.sort_recursive)
        test.test_selection_sort(selection_sort.sor_iterative_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
```

    Overwriting test_selection_sort.py

```python
%run -i test_selection_sort.py
```

    None input
    Empty input
    One element
    Two or more elements
    Success: test_selection_sort

    None input
    Empty input
    One element
    Two or more elements
