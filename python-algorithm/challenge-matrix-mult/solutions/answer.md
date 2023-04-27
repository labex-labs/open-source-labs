This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Given a list of 2x2 matrices, minimize the cost of matrix multiplication.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Do we just want to calculate the cost and not list the actual order of operations?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> Exception
- [] -> 0
- [Matrix(2, 3), Matrix(3, 6), Matrix(6, 4), Matrix(4, 5)] -> 124

## Algorithm

We'll use bottom up dynamic programming to build a table.

```txt

  0    1    2    3
[2,3][3,6][6,4][4,5]

Case: 0 * 1
2 * 3 * 6 = 36

Case: 1 * 2
3 * 6 * 4 = 72

Case: 2 * 3
6 * 4 * 5 = 120

Case: 0 * 1 * 2
0 * (1 * 2) = 2 * 3 * 4 + 72 = 96
(0 * 1) * 2 = 36 + 2 * 6 * 4 = 84
min: 84

Case: 1 * 2 * 3
1 * (2 * 3) = 3 * 6 * 5 + 120 = 210
(1 * 2) * 3 = 72 + 3 * 4 * 5 = 132
min: 132

Case: 0 * 1 * 2 * 3
0 * (1 * 2 * 3) = 2 * 3 * 5 + 132 = 162
(0 * 1) * (2 * 3) = 36 + 120 + 2 * 6 * 5 = 216
(0 * 1 * 2) * 3 = 84 + 2 * 4 * 5 = 124
min: 124

  ---------------------
  | 0 |  1 |  2 |   3 |
  ---------------------
0 | 0 | 36 | 84 | 124 |
1 | x |  0 | 72 | 132 |
2 | x |  x |  0 | 120 |
3 | x |  x |  x |   0 |
  ---------------------

min cost = T[0][cols-1] = 124

for k in range(i, j):
    T[i][j] = minimum of (T[i][k] + T[k+1][j] +
                          m[i].first * m[k].second * m[j].second) for all k
```

### Explanation of k

```txt
  0    1    2    3
[2,3][3,6][6,4][4,5]

Fill in the missing cell, where i = 0, j = 3

  ---------------------
  | 0 |  1 |  2 |   3 |
  ---------------------
0 | 0 | 36 | 84 | ??? |
1 | x |  0 | 72 | 132 |
2 | x |  x |  0 | 120 |
3 | x |  x |  x |   0 |
  ---------------------

Case: 0 * (1 * 2 * 3), k = 0
i = 0, j = 3

0 * (1 * 2 * 3) = 2 * 3 * 5 + 132 = 162
T[i][k] + T[k+1][j] + m[i].first * m[k].second * m[j].second
T[0][0] + T[1][3] + 2 * 3 * 5
0 + 132 + 30 = 162

Case: (0 * 1) * (2 * 3), k = 1
i = 0, j = 3

(0 * 1) * (2 * 3) = 36 + 120 + 2 * 6 * 5 = 216
T[i][k] + T[k+1][j] + m[i].first * m[k].second * m[j].second
T[0][1] + T[2][3] + 2 * 6 * 5
36 + 120 + 60 = 216

Case: (0 * 1 * 2) * 3, k = 2
i = 0, j = 3

(0 * 1 * 2) * 3 = 84 + 2 * 4 * 5 = 124
T[i][k] + T[k+1][j] + m[i].first * m[k].second * m[j].second
T[0][2] + T[3][3] + 2 * 4 * 5
84 + 0 + 40 = 124

```

Complexity:

- Time: O(n^3)
- Space: O(n^2)

## Code

```python
class Matrix(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second
```

```python
import sys


class MatrixMultiplicationCost(object):

    def find_min_cost(self, matrices):
        if matrices is None:
            raise TypeError('matrices cannot be None')
        if not matrices:
            return 0
        size = len(matrices)
        T = [[0] * size for _ in range(size)]
        for offset in range(1, size):
            for i in range(size-offset):
                j = i + offset
                min_cost = sys.maxsize
                for k in range(i, j):
                    cost = (T[i][k] + T[k+1][j] +
                            matrices[i].first *
                            matrices[k].second *
                            matrices[j].second)
                    if cost < min_cost:
                        min_cost = cost
                T[i][j] = min_cost
        return T[0][size-1]
```

## Unit Test

```python
%%writefile test_find_min_cost.py
import unittest


class TestMatrixMultiplicationCost(unittest.TestCase):

    def test_find_min_cost(self):
        matrix_mult_cost = MatrixMultiplicationCost()
        self.assertRaises(TypeError, matrix_mult_cost.find_min_cost, None)
        self.assertEqual(matrix_mult_cost.find_min_cost([]), 0)
        matrices = [Matrix(2, 3),
                    Matrix(3, 6),
                    Matrix(6, 4),
                    Matrix(4, 5)]
        expected_cost = 124
        self.assertEqual(matrix_mult_cost.find_min_cost(matrices), expected_cost)
        print('Success: test_find_min_cost')


def main():
    test = TestMatrixMultiplicationCost()
    test.test_find_min_cost()


if __name__ == '__main__':
    main()
```

    Overwriting test_find_min_cost.py

```python
%run -i test_find_min_cost.py
```

    Success: test_find_min_cost
