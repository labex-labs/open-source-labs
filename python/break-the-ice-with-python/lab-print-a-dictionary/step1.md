# Print a Dictionary

Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_a_dictionary.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_a_dictionary():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict)


print_a_dictionary()

```

This Python code defines a function called `print_a_dictionary`. Within the function, a dictionary is created using a dictionary comprehension.

The dictionary comprehension creates a dictionary where the keys are integers from 1 to 20, and the values are the squares of the corresponding keys.

The resulting dictionary is stored in the variable `dict`.

Finally, the resulting dictionary is printed to the console using the `print` function.

Overall, this code demonstrates how to use dictionary comprehensions in Python to create a dictionary with key-value pairs based on a given pattern or formula.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_a_dictionary.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18:
324, 19: 361, 20: 400}
```

At this point, your code is running successfully!
