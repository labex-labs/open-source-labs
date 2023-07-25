# Remove a Number from List

By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

## Preparation

Before we start writing the code, we should open the `/home/labex/project/remove_a_number_from_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def remove_a_number_from_list():
    li = [12, 24, 35, 24, 88, 120, 155]
    li = [x for x in li if x != 24]
    print(li)


remove_a_number_from_list()

```

This Python code defines a function called `remove_a_number_from_list`. Within the function, a list of integers `li` is defined with the values `[12, 24, 35, 24, 88, 120, 155]`.

A list comprehension is then used to create a new list that contains all the elements of `li` except for the value `24`. The list comprehension uses the syntax `[x for x in li if x != 24]`, which creates a new list by iterating over each element `x` in `li` and only including it in the new list if it is not equal to `24`.

Finally, the `print` function is used to print the resulting list to the console.

Overall, this code demonstrates how to use a list comprehension in Python to remove a specific value from a list of integers.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/remove_a_number_from_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[12, 35, 88, 120, 155]
```

At this point, your code is running successfully!
