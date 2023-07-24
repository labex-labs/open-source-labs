# Concatenate Two Strings

Define a function that can accept two strings as input and concatenate them and then print it in console.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/concatenate_two_strings.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def concatenate_two_strings(s1, s2):
    print(s1 + s2)


s1 = input()
s2 = input()
concatenate_two_strings(s1, s2)

```

This Python code demonstrates how to concatenate two strings. First, a function named `concatenate_two_strings` is defined, which takes two string parameters `s1` and `s2`.

Next, the `input` function is used to read two strings `s1` and `s2`. Then, the `concatenate_two_strings` function is called, and `s1` and `s2` are passed as arguments to it.

In the `concatenate_two_strings` function, the `+` operator is used to concatenate `s1` and `s2`, and the `print` function is used to print the result to the console.

Overall, this code demonstrates how to define and call a function, and how to concatenate two strings using the `+` operator.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/concatenate_two_strings.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
12
34
```

Then, the output of the program should be:

```bash
1234
```

At this point, your code is running successfully!
