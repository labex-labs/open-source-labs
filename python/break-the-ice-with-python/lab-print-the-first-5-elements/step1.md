# Print the First 5 Elements

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_the_first_5_elements.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_the_first_5_elements():
    lst = [i ** 2 for i in range(1, 21)]

    print(lst[:5])


print_the_first_5_elements()

```

This Python code defines a function called `print_the_first_5_elements`. Within the function, a list comprehension is used to create a list `lst` of the squares of the integers from `1` to `20`.

The list comprehension uses the syntax `[expression for variable in iterable]` to create a list of the squares of the integers. The expression `i ** 2` calculates the square of the current integer `i`, and the `range` function is used to generate the integers from `1` to `20`.

The resulting list `lst` contains the squares of the integers from `1` to `20`.

The `print` function is then used to print the first five elements of the list `lst` using slicing. The syntax `lst[:5]` returns a new list containing the first five elements of `lst`.

Overall, this code demonstrates how to use list comprehensions and slicing in Python to create and manipulate a list of the squares of the integers from `1` to `20`, and print the first five elements of the list.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_the_first_5_elements.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[1, 4, 9, 16, 25]
```

At this point, your code is running successfully!
