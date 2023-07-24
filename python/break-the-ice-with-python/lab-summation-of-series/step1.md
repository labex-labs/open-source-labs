# Summation of Series

Write a program to compute `1/2+2/3+3/4+...+n/n+1` with a given `n` input by console (n>0).

## Preparation

Before we start writing the code, we should open the `/home/labex/project/summation_of_series.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def summation_of_series():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i/(i+1)
    print(round(sum, 2))

    return round(sum, 2)


summation_of_series()

```

This Python code defines a function called `summation_of_series()` that calculates the summation of a series of numbers using a for loop. The function prompts the user to input a number `n` using the `input()` function and converts it to an integer using the `int()` function.

The function then initializes a variable called `sum` to `0` and uses a for loop to iterate over the range of numbers from `1` to `n+1`. For each number `i` in the range, the function adds `i/(i+1)` to the `sum` variable.

The function then uses the `round()` function to round the `sum` variable to two decimal places and prints the result to the console using the `print()` function.

Finally, the function returns the rounded `sum` variable.

The code then calls the `summation_of_series()` function to execute it and output the result to the console.

Overall, this code demonstrates how to use a for loop to calculate the summation of a series of numbers in Python. It also shows how to use the `round()` function to round a number to a specified number of decimal places.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/summation_of_series.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following n is given as input to the program:

```bash
5
```

Then, the output of the program should be:

```bash
3.55
```

At this point, your code is running successfully!
