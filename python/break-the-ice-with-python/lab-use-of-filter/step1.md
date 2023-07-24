# Use of Filter

Write a program which can `filter()` to make a list whose elements are even number between 1 and 20 (both included).

## Preparation

Before we start writing the code, we should open the `/home/labex/project/use_of_filter.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def even(x):
    return x % 2 == 0


def use_of_filter():
    evenNumbers = filter(even, range(1, 21))
    print(list(evenNumbers))


use_of_filter()

```

This Python code defines a function called `even()` that checks if a given number is even by using the modulo operator `%` to check if the remainder of the number divided by 2 is equal to 0. If the remainder is 0, the function returns `True`, indicating that the number is even. Otherwise, it returns `False`.

The code then defines another function called `use_of_filter()` that uses the `filter()` function to filter a range of numbers from 1 to 20 to only include the even numbers. The `filter()` function takes two arguments: the first is the function to apply to each element in the sequence, and the second is the sequence to filter. In this case, the `even()` function is applied to each element in the `range(1, 21)` sequence.

The filtered sequence of even numbers is then converted to a list using the `list()` function and printed to the console using the `print()` function.

Finally, the `use_of_filter()` function is called to execute it and print the even numbers from 1 to 20.

Overall, this code demonstrates how to use the `filter()` function in Python to filter a sequence based on a condition defined by a separate function. It also shows how to define a function to check if a number is even using the modulo operator `%`.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/use_of_filter.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

At this point, your code is running successfully!
