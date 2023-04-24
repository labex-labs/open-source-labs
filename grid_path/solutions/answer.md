This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement an algorithm to have a robot move from the upper left corner to the bottom right corner of a grid.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Are there restrictions to how the robot moves?
  - The robot can only move right and down
- Are some cells invalid (off limits)?
  - Yes
- Can we assume the starting and ending cells are valid cells?
  - Yes
- Is this a rectangular grid? i.e. the grid is not jagged?
  - Yes
- Will there always be a valid way for the robot to get to the bottom right?
  - No, return None
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

<pre>
o = valid cell
x = invalid cell

   0  1  2  3
0  o  o  o  o
1  o  x  o  o
2  o  o  x  o
3  x  o  o  o
4  o  o  x  o
5  o  o  o  x
6  o  x  o  x
7  o  x  o  o
</pre>

- General case

```
expected = [(0, 0), (1, 0), (2, 0),
            (2, 1), (3, 1), (4, 1),
            (5, 1), (5, 2), (6, 2),
            (7, 2), (7, 3)]
```

- No valid path, say row 7, col 2 is invalid
- None input
- Empty matrix

## Algorithm

To get to row r and column c [r, c], we will need to have gone:

- Right from [r, c-1] if this is a valid cell - [Path 1]
- Down from [r-1, c] if this is a valid cell - [Path 2]

If we look at [Path 1], to get to [r, c-1], we will need to have gone:

- Right from [r, c-2] if this is a valid cell
- Down from [r-1, c-1] if this is a valid cell

Continue this process until we reach the start cell or until we find that there is no path.

Base case:

- If the input row or col are < 0, or if [row, col] is not a valid cell
  - Return False

Recursive case:

We'll memoize the solution to improve performance.

- Use the memo to see if we've already processed the current cell
- If any of the following is True, append the current cell to the path and set our result to True:
  - We are at the start cell
  - We get a True result from a recursive call on:
    - [row, col-1]
    - [row-1, col]
- Update the memo
- Return the result

Complexity:

- Time: O(row \* col)
- Space: O(row \* col) for the recursion depth

## Code

```python
class Grid(object):

    def find_path(self, matrix):
        if matrix is None or not matrix:
            return None
        cache = {}
        path = []
        if self._find_path(matrix, len(matrix) - 1,
                           len(matrix[0]) - 1, cache, path):
            return path
        else:
            return None

    def _find_path(self, matrix, row, col, cache, path):
        if row < 0 or col < 0 or not matrix[row][col]:
            return False
        cell = (row, col)
        if cell in cache:
            return cache[cell]
        cache[cell] = (row == 0 and col == 0 or
                       self._find_path(matrix, row, col - 1, cache, path) or
                       self._find_path(matrix, row - 1, col, cache, path))
        if cache[cell]:
            path.append(cell)
        return cache[cell]
```

## Unit Test

```python
%%writefile test_grid_path.py
import unittest


class TestGridPath(unittest.TestCase):

    def test_grid_path(self):
        grid = Grid()
        self.assertEqual(grid.find_path(None), None)
        self.assertEqual(grid.find_path([[]]), None)
        max_rows = 8
        max_cols = 4
        matrix = [[1] * max_cols for _ in range(max_rows)]
        matrix[1][1] = 0
        matrix[2][2] = 0
        matrix[3][0] = 0
        matrix[4][2] = 0
        matrix[5][3] = 0
        matrix[6][1] = 0
        matrix[6][3] = 0
        matrix[7][1] = 0
        result = grid.find_path(matrix)
        expected = [(0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (4, 1),
                    (5, 1), (5, 2), (6, 2),
                    (7, 2), (7, 3)]
        self.assertEqual(result, expected)
        matrix[7][2] = 0
        result = grid.find_path(matrix)
        self.assertEqual(result, None)
        print('Success: test_grid_path')


def main():
    test = TestGridPath()
    test.test_grid_path()


if __name__ == '__main__':
    main()
```

    Overwriting test_grid_path.py

```python
%run -i test_grid_path.py
```

    Success: test_grid_path
