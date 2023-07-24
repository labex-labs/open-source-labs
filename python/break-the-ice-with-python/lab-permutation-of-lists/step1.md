# Permutation of Lists

Please write a program which prints all permutations of [1,2,3].

## Preparation

Before we start writing the code, we should open the `/home/labex/project/permutation_of_lists.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
from itertools import permutations


def permutation_of_lists(iterable):
    p = permutations(iterable)
    for i in p:
        print(i)


x = [1, 2, 3]
permutation_of_lists(x)

```

This Python code defines a function called `permutation_of_lists` that takes an iterable as input. Within the function, the `permutations` function from the `itertools` module is used to generate all possible permutations of the input iterable.

A `for` loop is then used to iterate over each permutation and print it to the console using the `print` function.

In the main program, a list `[1, 2, 3]` is defined and passed as an argument to the `permutation_of_lists` function. The function generates all possible permutations of the list and prints them to the console.

Overall, this code demonstrates how to use the `permutations` function from the `itertools` module in Python to generate all possible permutations of an iterable.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/permutation_of_lists.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If you are given the following list:

```bash
[1, 2, 3]
```

Then, the output of the program should be:

```bash
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
```

At this point, your code is running successfully!
