# Grid Path

## Problem

Given a rectangular grid with valid and invalid cells, implement a function to find a valid path for the robot to move from the upper left corner to the bottom right corner. If there is no valid path, return None. If the input is invalid or the matrix is empty, return None.

## Requirements

The requirements for this algorithm are as follows:

- The robot can only move right and down.
- Some cells may be off-limits.
- The grid is rectangular and not jagged.
- There may not always be a valid path for the robot to reach the bottom right corner.
- The input may not always be valid.
- The algorithm should fit within memory constraints.

## Example Usage

Consider the following grid:

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

- General case:

```
expected = [(0, 0), (1, 0), (2, 0),
            (2, 1), (3, 1), (4, 1),
            (5, 1), (5, 2), (6, 2),
            (7, 2), (7, 3)]
```

- No valid path: In the above example, row 7 col 2 is also invalid -> None
- None input -> None
- Empty matrix -> None
