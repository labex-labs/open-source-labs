# Grid Path

Problem: Implement an algorithm to have a robot move from the upper left corner to the bottom right corner of a grid.

## Requirements

- Are there restrictions to how the robot moves?
  - The robot can only move right and down
- Are some cells off limits?
  - Yes
- Is this a rectangular grid? i.e. the grid is not jagged?
  - Yes
- Will there always be a valid way for the robot to get to the bottom right?
  - No, return None
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

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

- No valid path: In above example, row 7 col 2 is also invalid -> None
- None input -> None
- Empty matrix -> None
