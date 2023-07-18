# Print the Longest String

Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_the_longest_string.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_the_longest_string(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)


s1, s2 = input().split()
print_the_longest_string(s1, s2)

```

This Python code defines a function called `print_the_longest_string` that takes two strings `s1` and `s2` as input. Within the function, the lengths of the two strings calculated using the `len` function and stored in the variables `len1` and `len2`, respectively.

An `if` statement is then used to compare the lengths of the two strings. If `len1` is greater than `len2`, the function prints `s1` using the `print` function. If `len1` is less than `len2`, the function prints `s2`. If the lengths are equal, the function prints both `s1` and `s2` using two separate `print` statements.

The main part of the code prompts the user to enter two strings `s1` and `s2`, which are separated by a space and read using the `input` function and the `split` method. The resulting strings are then passed as arguments to the `print_the_longest_string` function.

Overall, this code demonstrates how to use the `len` function and an `if` statement in Python to compare the lengths of two strings and print the longest string or both strings if they have the same length.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_the_longest_string.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
abcdef 1234
```

Then, the output of the program should be:

```bash
abcdef
```

At this point, your code is running successfully!
