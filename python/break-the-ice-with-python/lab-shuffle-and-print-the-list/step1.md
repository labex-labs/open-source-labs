# Shuffle and Print the List

Please write a program to shuffle and print the list [3,6,7,8].

## Preparation

Before we start writing the code, we should open the `/home/labex/project/shuffle_and_print_the_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import random


def shuffle_and_print_the_list():
    lst = [3, 6, 7, 8]
    random.shuffle(lst)
    print(lst)


shuffle_and_print_the_list()

```

This Python code defines a function called `shuffle_and_print_the_list()` that shuffles a list of integers and prints the shuffled list to the console. The function creates a list called `lst` containing the integers `[3, 6, 7, 8]`.

The function then uses the `shuffle()` function from the `random` module to shuffle the elements in the list `lst`. The `shuffle()` function randomly reorders the elements in the list.

Finally, the function uses the `print()` function to output the shuffled `lst` list to the console.

Overall, this code demonstrates how to use the `shuffle()` function from the `random` module to shuffle the elements in a list of integers in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/shuffle_and_print_the_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
[6, 7, 8, 3]
```

At this point, your code is running successfully!
