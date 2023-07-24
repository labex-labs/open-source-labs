# Generate Random Integer Number

Please write a program to randomly print a integer number between 7 and 15 inclusive.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_random_integer_number.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import random


def generate_random_integer_number():
    print(random.randrange(7, 16))


generate_random_integer_number()

```

This Python code defines a function called `generate_random_integer_number`. Within the function, a random integer number is generated using the `random.randrange` function.

The `random.randrange` function takes two arguments: a start value and a stop value. It returns a random integer number between the start value (inclusive) and the stop value (exclusive).

In this case, the start value is 7 and the stop value is 16, so the resulting random integer number will be between 7 (inclusive) and 16 (exclusive).

The resulting random integer number is printed to the console using the `print` function.

Overall, this code demonstrates how to use the `random.randrange` function in Python to generate a random integer number within a specific range.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_random_integer_number.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
15
```

At this point, your code is running successfully!
