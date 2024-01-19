# Solution Notebook

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement the [Towers of Hanoi](http://en.wikipedia.org/wiki/Tower_of_Hanoi) with 3 towers and N disks.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume we already have a stack class that can be used for this problem?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None tower(s) -> Exception
- 0 disks -> None
- 1 disk
- 2 or more disks

## Algorithm

- Create three stacks to represent each tower
- def hanoi(n, src, dest, buffer):
  - If 0 disks return
  - hanoi(n-1, src, buffer, dest)
  - Move remaining element from src to dest
  - hanoi(n-1, buffer, dest, src)

Complexity:

- Time: O(2^n)
- Space: O(m) where m is the number of recursion levels

## Code

```python
%run ../../stacks_queues/stack/stack.py
```

```python
class Hanoi(object):

    def move_disks(self, num_disks, src, dest, buff):
        if src is None or dest is None or buff is None:
            raise TypeError('Cannot have a None input')
        self._move_disks(num_disks, src, dest, buff)

    def _move_disks(self, num_disks, src, dest, buff):
        if num_disks == 0:
            return
        self.move_disks(num_disks - 1, src, buff, dest)
        dest.push(src.pop())
        self.move_disks(num_disks - 1, buff, dest, src)
```

## Unit Test

```python
%%writefile test_hanoi.py
import unittest


class TestHanoi(unittest.TestCase):

    def test_hanoi(self):
        hanoi = Hanoi()
        num_disks = 3
        src = Stack()
        buff = Stack()
        dest = Stack()

        print('Test: None towers')
        self.assertRaises(TypeError, hanoi.move_disks, num_disks, None, None, None)

        print('Test: 0 disks')
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), None)

        print('Test: 1 disk')
        src.push(5)
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), 5)

        print('Test: 2 or more disks')
        for disk_index in range(num_disks, -1, -1):
            src.push(disk_index)
        hanoi.move_disks(num_disks, src, dest, buff)
        for disk_index in range(0, num_disks):
            self.assertEqual(dest.pop(), disk_index)

        print('Success: test_hanoi')


def main():
    test = TestHanoi()
    test.test_hanoi()


if __name__ == '__main__':
    main()
```

    Overwriting test_hanoi.py

```python
%run -i test_hanoi.py
```

    Test: None towers
    Test: 0 disks
    Test: 1 disk
    Test: 2 or more disks
    Success: test_hanoi
