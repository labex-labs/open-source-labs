# Calculate the Factorial

Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculate_the_factorial.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def calculate_the_factorial():
    n = int(input())
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)


calculate_the_factorial()

```

This Python code implements a function called `calculate_the_factorial` that calculates the factorial of an integer entered by the user. It reads the integer from user input using the `input()` function and converts it to an integer using the `int()` function. The function then initializes a variable called `fact` to 1 and uses a `for` loop to iterate from 1 to `n`, multiplying `fact` by the current iteration value `i` and storing the result back in `fact` at each iteration. The function then prints the final value of `fact` to the console using the `print()` function. The function is called at the end to calculate the factorial of the integer entered by the user.

Overall, this code provides a simple way to calculate the factorial of an integer entered by the user using Python's built-in functions and a `for` loop.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculate_the_factorial.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
8
```

Then, the output of the program should be:

```bash
40320
```

At this point, your code is running successfully!
