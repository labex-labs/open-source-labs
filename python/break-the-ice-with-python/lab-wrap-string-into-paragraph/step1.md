# Wrap String into Paragraph

You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/wrap_string_into_paragraph.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
from textwrap import wrap


def wrap_string_into_paragraph():
    S = str(input())
    w = int(input())
    z = list(wrap(S, w))

    for i in z:
        print(i)


wrap_string_into_paragraph()

```

This Python code defines a function called `wrap_string_into_paragraph()` that wraps a given string into paragraphs of a specified width. The function prompts the user to input a string `S` and an integer `w` representing the width of each paragraph.

The function then uses the `wrap()` function from the `textwrap` module to wrap the string `S` into a list of paragraphs with a width of `w`. The resulting list of paragraphs is stored in a variable `z`.

Finally, the function uses a `for` loop to iterate over each paragraph in the list `z` and print it to the console using the `print()` function.

The `wrap_string_into_paragraph()` function is then called to execute it and prompt the user for input.

Overall, this code demonstrates how to use the `wrap()` function from the `textwrap` module in Python to wrap a string into paragraphs of a specified width. It also shows how to use a `for` loop to iterate over a list and print each element to the console using the `print()` function.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/wrap_string_into_paragraph.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```

Then, the output of the program should be:

```bash
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```

At this point, your code is running successfully!
