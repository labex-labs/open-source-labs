# Generate a Special Number List

Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_a_special_number_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import random


def generate_a_special_number_list():
    lst = [i for i in range(1, 1001) if i % 35 == 0]
    resp = random.sample(lst, 5)
    print(resp)


generate_a_special_number_list()

```

This Python code defines a function called `generate_a_special_number_list`. Within the function, a list of special numbers is generated using a list comprehension.

The list comprehension creates a list of numbers between 1 and 1000 (inclusive) that are divisible by both 5 and 7 (i.e., numbers that are multiples of 35).

A list of 5 random elements is then selected from the list of special numbers using the `random.sample` function.

The resulting list of 5 random special numbers is stored in the variable `resp`.

Finally, the resulting list is printed to the console using the `print` function.

Overall, this code demonstrates how to use a list comprehension in Python to generate a list of special numbers that meet a specific condition, and how to use the `random.sample` function to select a random subset of elements from the list.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_a_special_number_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
[665, 35, 805, 980, 560]
```

At this point, your code is running successfully!
