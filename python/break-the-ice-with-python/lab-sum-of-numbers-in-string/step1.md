# Sum of Numbers in String

Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/sum_of_numbers_in_string.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def sum_of_numbers_in_string(s1, s2):
    print(int(s1) + int(s2))


s1 = input()
s2 = input()
sum_of_numbers_in_string(s1, s2)

```

This Python code defines a function called `sum_of_numbers_in_string()` that takes two string arguments `s1` and `s2`, converts them to integers using the `int()` function, and then adds them together using the `+` operator. The resulting sum is then printed to the console using the `print()` function.

The code then prompts the user to input two strings `s1` and `s2` using the `input()` function.

Finally, the `sum_of_numbers_in_string()` function is called with the `s1` and `s2` strings as arguments, and the resulting sum is printed to the console.

Overall, this code demonstrates how to convert strings to integers and perform arithmetic operations on them in Python. It also shows how to define and call a function with arguments in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/sum_of_numbers_in_string.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
3
4
```

Then, the output of the program should be:

```bash
7
```

At this point, your code is running successfully!
