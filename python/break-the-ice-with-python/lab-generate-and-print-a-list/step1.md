# Generate and Print a List

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_and_print_a_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def generate_and_print_a_list():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)


generate_and_print_a_list()

```

This Python code defines a function called `generate_and_print_a_list`. Within the function, a list of squared numbers is generated using a list comprehension.

The list comprehension creates a list of the squares of numbers between 1 and 20 (inclusive).

The resulting list of squared numbers is stored in the variable `lst`.

Finally, the resulting list is printed to the console using the `print` function.

Overall, this code demonstrates how to use a list comprehension in Python to generate a list of squared numbers, and how to use the `print` function to display the resulting list.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_and_print_a_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
```

At this point, your code is running successfully!
