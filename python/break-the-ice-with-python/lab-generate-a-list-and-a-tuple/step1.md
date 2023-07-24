# Generate a List and a Tuple

Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_a_list_and_a_tuple.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def generate_a_list_and_a_tuple():
    lst = input().split(',')
    tpl = tuple(lst)

    print(lst)
    print(tpl)


generate_a_list_and_a_tuple()

```

This Python code defines a function called `generate_a_list_and_a_tuple`. Within the function, the user is prompted to enter a comma-separated list of values using the `input` function. The `split` method is then used to split the input string into a list of individual values, using the comma as the delimiter.

A tuple is then created from the list using the `tuple` function.

Finally, both the list and the tuple are printed to the console using the `print` function.

Overall, this code demonstrates how to use the `input` function and the `split` method in Python to read a comma-separated list of values from the user, and how to convert the resulting list to a tuple using the `tuple` function.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_a_list_and_a_tuple.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
34,67,55,33,12,98
```

Then, the output of the program should be:

```bash
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```

At this point, your code is running successfully!
