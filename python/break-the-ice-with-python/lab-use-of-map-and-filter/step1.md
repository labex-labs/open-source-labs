# Use of Map and Filter

Write a program which can `map()` and `filter()` to make a list whose elements are square of even number in `[1,2,3,4,5,6,7,8,9,10]`.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/use_of_map_and_filter.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def even(x):
    return x % 2 == 0


def squer(x):
    return x*x


def use_of_map_and_filter():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # first filters number by even number and the apply map() on the resultant elements
    li = map(squer, filter(even, li))
    print(list(li))


use_of_map_and_filter()

```

This Python code defines two functions: `even()` and `squer()`. The `even()` function checks if a given number is even by using the modulo operator `%` to check if the remainder of the number divided by 2 is equal to 0. If the remainder is 0, the function returns `True`, indicating that the number is even. Otherwise, it returns `False`. The `squer()` function calculates the square of a given number by multiplying it by itself. The function takes a single argument `x` and returns the result of `x*x`.

The code then defines another function called `use_of_map_and_filter()` that demonstrates how to use the `map()` and `filter()` functions together to apply a function to a filtered sequence of elements. The function creates a list `li` containing the numbers from 1 to 10.

The function then uses the `filter()` function to filter the even numbers from the list `li`. The resulting filtered sequence is then passed to the `map()` function, which applies the `squer()` function to each element in the filtered sequence. The resulting sequence of squared even numbers is then converted to a list using the `list()` function and printed to the console using the `print()` function.

Finally, the `use_of_map_and_filter()` function is called to execute it and print the squared even numbers from 1 to 10.

Overall, this code demonstrates how to use the `map()` and `filter()` functions together in Python to apply a function to a filtered sequence of elements. It also shows how to define functions to check if a number is even and calculate the square of a number using the modulo operator `%` and the multiplication operator `*`, respectively.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/use_of_map_and_filter.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[4, 16, 36, 64, 100]
```

At this point, your code is running successfully!
