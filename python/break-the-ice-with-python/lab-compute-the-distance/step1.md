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

## Preparation

Before we start writing the code, we should open the `/home/labex/project/compute_the_distance.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import math


def compute_the_distance():
    x, y = 0, 0
    while True:
        s = input().split()
        if not s:
            break
        if s[0] == 'UP':                  # s[0] indicates command
            x -= int(s[1])                # s[1] indicates unit of move
        if s[0] == 'DOWN':
            x += int(s[1])
        if s[0] == 'LEFT':
            y -= int(s[1])
        if s[0] == 'RIGHT':
            y += int(s[1])
            # N**P means N^P
    # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
    dist = round(math.sqrt(x**2 + y**2))
    print(dist)


compute_the_distance()

```

This Python code demonstrates how to calculate the distance traveled on a plane. First, a function named `compute_the_distance` is defined, which initializes variables `x` and `y` to 0.

Next, an infinite loop is used to read user input commands until an empty line is entered. Each command is a string consisting of two parts: an instruction and a number, separated by a space. Depending on the instruction, the values of `x` and `y` are updated to simulate movement on the plane.

Finally, the Euclidean distance formula is used to calculate the distance from the origin to the final position, and the result is rounded to the nearest integer. The Euclidean distance formula is the formula for calculating the distance between two points on a plane, which is $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$. Here, the values of $x_1$ and $y_1$ are 0, and the values of $x_2$ and $y_2$ are the final values of `x` and `y`. Finally, the `print` function is used to print the calculated distance to the console.

Overall, this code demonstrates how to use Python's `math` module to calculate Euclidean distance, and shows how to use loops and conditional statements to simulate movement on a plane.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/compute_the_distance.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

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

At this point, your code is running successfully!
