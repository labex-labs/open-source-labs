# Print such Numbers

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 2200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_such_numbers.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_such_numbers():
    for i in range(2000, 2201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')


print_such_numbers()

```

This Python code defines a function called `print_such_numbers`. Within the function, a `for` loop is used to iterate over the integers from `2000` to `2200`.

The statement checks if the current integer`i`is divisible by`7`using the modulo operator`%`, and also checks if it is not divisible by `5`using the`!=`operator. If both conditions are true, the integer`i`is printed to the console using the`print`function with the`end`parameter set to`','`.

The `end` parameter is used to specify the string that should be printed at the end of the `print` statement. By default, the `end` parameter is set to `'\n'`, which prints a newline character at the end of the statement. In this case, the `end` parameter is set to `','` to print a comma separator between the numbers.

Overall, this code demonstrates how to use a `for` loop and an `if` statement in Python to iterate over a range of integers and print only the numbers that meet certain conditions. In this case, the function prints all the numbers between `2000` and `2200` that are divisible by `7` but not divisible by `5`.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_such_numbers.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The output of the program should be:

```bash
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,
```

At this point, your code is running successfully!
