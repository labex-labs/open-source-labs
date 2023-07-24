# Remove Even Numbers from List

Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

## Preparation

Before we start writing the code, we should open the `/home/labex/project/remove_even_numbers_from_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def is_even(n):
    return n % 2 != 0


def remove_even_numbers_from_list():
    li = [5, 6, 77, 45, 22, 12, 24]
    lst = list(filter(is_even, li))
    print(lst)


remove_even_numbers_from_list()

```

This Python code defines two functions: `is_even(n)` and `remove_even_numbers_from_list()`.

The `is_even(n)` function takes an integer `n` as a parameter and returns a boolean value indicating whether the integer is even. If `n` is even, it returns `True`; otherwise, it returns `False`.

The `remove_even_numbers_from_list()` function creates a list of integers called `li` that contains both even and odd numbers. It then uses Python's built-in `filter()` function and the `is_even()` function to filter out all the even numbers from the list. The `filter()` function takes a function and an iterable as arguments and returns a new iterable that contains only the elements for which the function returns `True`. In this example, the `filter()` function uses the `is_even()` function to determine whether each element in the list is even, and then returns a new list called `lst` that contains only the odd numbers.

Finally, the `remove_even_numbers_from_list()` function uses the `print()` function to output the new list `lst` to the console.

Overall, this code demonstrates how to use the `filter()` function and a custom function to filter out all the even numbers from a list of integers.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/remove_even_numbers_from_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[5, 77, 45]
```

At this point, your code is running successfully!
