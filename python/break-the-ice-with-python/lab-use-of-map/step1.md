# Use of Map

Write a program which can `map()` to make a list whose elements are square of numbers between 1 and 20 (both included).

## Preparation

Before we start writing the code, we should open the `/home/labex/project/use_of_map.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def sqr(x):
    return x*x


def use_of_map():
    squaredNumbers = list(map(sqr, range(1, 21)))
    print(squaredNumbers)


use_of_map()

```

This Python code defines a function called `sqr()` that calculates the square of a given number by multiplying it by itself. The function takes a single argument `x` and returns the result of `x*x`.

The code then defines another function called `use_of_map()` that uses the `map()` function to apply the `sqr()` function to each element in a range of numbers from 1 to 20. The `map()` function takes two arguments: the first is the function to apply to each element in the sequence, and the second is the sequence to map. In this case, the `sqr()` function is applied to each element in the `range(1, 21)` sequence.

The resulting sequence of squared numbers is then converted to a list using the `list()` function and printed to the console using the `print()` function.

Finally, the `use_of_map()` function is called to execute it and print the squared numbers from 1 to 20.

Overall, this code demonstrates how to use the `map()` function in Python to apply a function to each element in a sequence and return a new sequence with the results. It also shows how to define a function to calculate the square of a number using the multiplication operator `*`.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/use_of_map.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
```

At this point, your code is running successfully!
