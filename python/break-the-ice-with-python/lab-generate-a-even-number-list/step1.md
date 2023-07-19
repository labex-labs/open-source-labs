# Generate a Even Number List

Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_a_even_number_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import random


def generate_a_even_number_list():
    resp = random.sample(range(100, 201, 2), 5)
    print(resp)


generate_a_even_number_list()

```

This Python code defines a function called `generate_a_even_number_list`. Within the function, a list of even numbers is generated using the `random.sample` function.

The `range` function is used to generate a sequence of even numbers between 100 and 200 (inclusive) with a step of 2. This sequence is passed as the first argument to `random.sample`.

The second argument to `random.sample` is the number of elements to be selected from the sequence. In this case, 5 elements are selected at random from the sequence.

The resulting list of 5 even numbers is stored in the variable `resp`.

Finally, the resulting list is printed to the console using the `print` function.

Overall, this code demonstrates how to use the `random.sample` function in Python to generate a list of even numbers within a specific range.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_a_even_number_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
[122, 200, 142, 182, 154]
```

At this point, your code is running successfully!
