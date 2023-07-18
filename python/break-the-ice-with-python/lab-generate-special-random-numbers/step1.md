# Generate Special Random Numbers

Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_special_random_numbers.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import random


def generate_special_random_numbers():
    resp = [i for i in range(10, 151) if i % 35 == 0]
    print(random.choice(resp))


generate_special_random_numbers()

```

This Python code defines a function called `generate_special_random_numbers`. Within the function, a list of special numbers is generated using a list comprehension.

The list comprehension creates a list of numbers between 10 and 150 (inclusive) that are divisible by both 5 and 7 (i.e., numbers that are multiples of 35).

A random special number is then selected from the list using the `random.choice` function.

The resulting random special number is printed to the console using the `print` function.

Overall, this code demonstrates how to use a list comprehension in Python to generate a list of special numbers that meet a specific condition, and how to use the `random.choice` function to select a random element from the list.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_special_random_numbers.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
105
```

At this point, your code is running successfully!
