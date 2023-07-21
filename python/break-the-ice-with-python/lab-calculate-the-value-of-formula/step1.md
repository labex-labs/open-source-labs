# Calculate the Value of Formula

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculate_the_value_of_formula.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
from math import sqrt


def calculate_the_value_of_formula():
    C, H = 50, 30

    def calc(D):
        return sqrt((2*C*D)/H)

    D = input().split(',')
    D = [str(round(calc(int(i)))) for i in D]
    print(",".join(D))


calculate_the_value_of_formula()

```

This Python code defines a function called `calculate_the_value_of_formula` that calculates the value of a formula for a given input. The formula involves calculating the square root of (2*C*D)/H, where C and H are constants with values of 50 and 30, respectively, and D is the input value. The function reads the input value as a comma-separated string using the `input()` function and splits it into a list using the `split()` method. It then uses a list comprehension to apply the formula to each element of the list, rounding the result to the nearest integer using the `round()` function and converting it back to a string using the `str()` function. Finally, it joins the resulting list of strings back into a comma-separated string using the `join()` method and prints it to the console using the `print()` function.

Overall, this code provides a simple way to calculate the value of a formula for a given input using Python's built-in functions and a list comprehension.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculate_the_value_of_formula.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
100,150,180
```

Then, the output of the program should be:

```bash
18,22,24
```

At this point, your code is running successfully!
