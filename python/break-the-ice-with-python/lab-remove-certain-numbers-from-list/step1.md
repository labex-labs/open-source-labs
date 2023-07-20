# Remove Certain Numbers from List

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

## Preparation

Before we start writing the code, we should open the `/home/labex/project/remove_certain_numbers_from_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def remove_certain_numbers_from_list():
    orig_lst = [12, 24, 35, 70, 88, 120, 155]
    indices = [0, 2, 4, 6]

    new_list = [i for (j, i) in enumerate(orig_lst) if j not in indices]
    print(new_list)


remove_certain_numbers_from_list()

```

This Python code defines a function called `remove_certain_numbers_from_list` that removes certain numbers from a list of integers. The function creates a list called `orig_lst` containing the integers `[12, 24, 35, 70, 88, 120, 155]`, and a list called `indices` containing the indices of the elements to be removed, which are `[0, 2, 4, 6]`.

The function then uses a list comprehension to create a new list called `new_list` that contains all the elements of `orig_lst` except for those at the indices specified in `indices`. The list comprehension uses the `enumerate()` function to iterate over the elements of `orig_lst` along with their indices, and an `if` statement to check if the current index is in the `indices` list. If the index is not in the list, the corresponding element is added to `new_list`.

Finally, the function prints `new_list` to the console using the `print()` function.

In summary, this code demonstrates how to remove certain elements from a list of integers in Python using a list comprehension and the `enumerate()` function.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/remove_certain_numbers_from_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[24, 70, 120]
```

At this point, your code is running successfully!
