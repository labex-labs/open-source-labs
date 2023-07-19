# Print a Tuple

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_a_tuple.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_a_tuple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))


print_a_tuple()

```

This Python code defines a function called `print_a_tuple`. Within the function, a list is created using a list comprehension.

The list comprehension creates a list where the elements are the squares of integers from 1 to 20.

The resulting list is stored in the variable `lst`.

The `tuple` function is then used to convert the list `lst` into a tuple.

Finally, the resulting tuple is printed to the console using the `print` function.

Overall, this code demonstrates how to use list comprehensions in Python to create a list with elements based on a given pattern or formula, and how to convert a list to a tuple using the `tuple` function.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_a_tuple.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)
```

At this point, your code is running successfully!
