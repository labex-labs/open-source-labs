# Calculate Square Value

Write a method which can calculate square value of number.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculate_square_value.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def calculate_square_value():
    n = int(input())
    print(n**2)


calculate_square_value()

```

This Python code implements a function called `calculate_square_value` that calculates the square value of an integer entered by the user. It reads the integer from user input using the `input()` function and converts it to an integer using the `int()` function. The function then calculates the square value of the integer using the `**` operator which can be written as `n**p` where means `n^p` and prints the result to the console using the `print()` function. The function is called at the end to calculate the square value of the integer entered by the user.

Overall, this code provides a simple way to calculate the square value of an integer entered by the user using Python's built-in functions.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculate_square_value.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
2
```

Then, the output of the program should be:

```bash
4
```

At this point, your code is running successfully!
