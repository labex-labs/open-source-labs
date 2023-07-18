# Generate Random Float

Please generate a random float where the value is between 10 and 100 using Python module.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_random_float.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import random


def generate_random_float():

    rand_num = random.uniform(10, 100)
    print(rand_num)


generate_random_float()

```

This Python code defines a function called `generate_random_float`. Within the function, a random floating-point number is generated using the `random.uniform` function.

The `random.uniform` function takes two arguments: a lower bound and an upper bound. It returns a random floating-point number between the two bounds, inclusive of the lower bound but exclusive of the upper bound.

In this case, the lower bound is 10 and the upper bound is 100, so the resulting random floating-point number will be between 10 and 100 (inclusive of 10 but exclusive of 100).

The resulting random floating-point number is stored in the variable `rand_num`.

Finally, the resulting random floating-point number is printed to the console using the `print` function.

Overall, this code demonstrates how to use the `random.uniform` function in Python to generate a random floating-point number within a specific range.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_random_float.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The output of the program may be:

```bash
56.79468635168542
```

At this point, your code is running successfully!
