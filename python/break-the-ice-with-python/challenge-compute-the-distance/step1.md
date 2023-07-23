# Compute the Distance

A robot moves in a plane starting from the original point (0,0). The robot can move toward `UP`, `DOWN`, `LEFT` and `RIGHT` with a given steps. The trace of robot movement is shown as the following:

```bash
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

The numbers after the direction are steps.

Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

## Example

Suppose the following input is supplied to the program:

```bash
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

Then, the output of the program should be:

```bash
2
```

## Hints

- In case of input data being supplied to the program, it should be assumed to be a console input.
- Here distance indicates to euclidean distance.
- Import `math` module to use `sqrt` function.
