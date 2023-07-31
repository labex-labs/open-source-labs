# Generate Random Even Number

Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_random_even_number.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import random


def generate_random_even_number():
    resp = [i for i in range(0, 11, 2)]
    print(random.choice(resp))


generate_random_even_number()

```

This Python code defines a function called `generate_random_even_number`. Within the function, a list of even numbers is generated using a list comprehension.

The list comprehension creates a list of even numbers between 0 and 10 (inclusive) with a step of 2.

A random even number is then selected from the list using the `random.choice` function.

The resulting random even number is printed to the console using the `print` function.

Overall, this code demonstrates how to use a list comprehension in Python to generate a list of even numbers, and how to use the `random.choice` function to select a random element from the list.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_random_even_number.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
6
```

At this point, your code is running successfully!
