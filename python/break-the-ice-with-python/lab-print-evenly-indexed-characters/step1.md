# Print Evenly Indexed Characters

Please write a program which accepts a string from console and print the characters that have even indexes.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_evenly_indexed_characters.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_evenly_indexed_characters():
    s = "H1e2l3l4o5w6o7r8l9d"
    s = [s[i] for i in range(len(s)) if i % 2 == 0]
    print(''.join(s))


print_evenly_indexed_characters()

```

This Python code defines a function called `print_evenly_indexed_characters`. Within the function, a string `s` is initialized with a sequence of characters.

A list comprehension is then used to create a new list `s` that contains only the characters of the original string `s` that have an even index. The `range` function is used to generate a sequence of integers from 0 to the length of the string `s`, and the `%` operator is used to check if the index is even. If it is, the corresponding character is added to the new list `s`.

Finally, the elements of the `s` list are joined together using the `join` method with an empty string as the separator, and the resulting string is printed to the console using the `print` function.

Overall, this code demonstrates how to use list comprehensions in Python to create a new list that contains only the elements of an original list that satisfy a certain condition, and how to use the `join` method to concatenate the elements of a list into a string.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_evenly_indexed_characters.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
Helloworld
```

At this point, your code is running successfully!
