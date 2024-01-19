# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Create a list for each level of a binary tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is this a binary search tree?
  - Yes
- Should each level be a list of nodes?
  - Yes
- Can we assume we already have a Node class with an insert method?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- 5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11 -> [[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]

Note: Each number in the result is actually a node containing the number

## Algorithm

We can use either a depth-first or a breadth-first search. Intuitively, it seems like a breadth-first search might be a better fit as we are creating a linked list for each level.

We can use a modified breadth-first search that keeps track of parents as we build the linked list for the current level.

- Append the root to the current level's linked list `current`
- While the `current` is not empty:
  - Add `current` to `results`
  - Set `parents` to `current` to prepare to go one level deeper
  - Clear `current` so it can hold the next level
  - For each `parent` in `parents`, add the children to `current`
- Return the results

Complexity:

- Time: O(n)
- Space: O(n)

## Code

```python
%run ../bst/bst.py
```

```python
class BstLevelLists(Bst):

    def create_level_lists(self):
        if self.root is None:
            return
        results = []
        current = []
        parents = []
        current.append(self.root)
        while current:
            results.append(current)
            parents = list(current)
            current = []
            for parent in parents:
                if parent.left is not None:
                    current.append(parent.left)
                if parent.right is not None:
                    current.append(parent.right)
        return results
```

## Unit Test

```python
%run ../utils/results.py
```

```python
%%writefile test_tree_level_lists.py
import unittest


class TestTreeLevelLists(unittest.TestCase):

    def test_tree_level_lists(self):
        bst = BstLevelLists(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(2)
        bst.insert(4)
        bst.insert(1)
        bst.insert(7)
        bst.insert(6)
        bst.insert(9)
        bst.insert(10)
        bst.insert(11)

        levels = bst.create_level_lists()
        results_list = []
        for level in levels:
            results = Results()
            for node in level:
                results.add_result(node)
            results_list.append(results)

        self.assertEqual(str(results_list[0]), '[5]')
        self.assertEqual(str(results_list[1]), '[3, 8]')
        self.assertEqual(str(results_list[2]), '[2, 4, 7, 9]')
        self.assertEqual(str(results_list[3]), '[1, 6, 10]')
        self.assertEqual(str(results_list[4]), '[11]')

        print('Success: test_tree_level_lists')


def main():
    test = TestTreeLevelLists()
    test.test_tree_level_lists()


if __name__ == '__main__':
    main()
```

    Overwriting test_tree_level_lists.py

```python
%run -i test_tree_level_lists.py
```

    Success: test_tree_level_lists
