# Remove Several Numbers from List

By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

## Preparation

Before we start writing the code, we should open the `/home/labex/project/remove_several_numbers_from_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def remove_several_numbers_from_list():
    orig_list = [12, 24, 35, 70, 88, 120, 155]
    new_list = [i for (j, i) in enumerate(orig_list) if j not in range(1, 4)]
    print(new_list)


remove_several_numbers_from_list()

```

This Python code defines a function called `remove_several_numbers_from_list()` that removes several numbers from a list of integers. The function creates a list called `orig_list` containing the integers `[12, 24, 35, 70, 88, 120, 155]`.

The function then uses a list comprehension to create a new list called `new_list` that contains all the elements from `orig_list` except for the elements at indices 1, 2, and 3. The `enumerate()` function is used to iterate over the elements of `orig_list` along with their indices. The `range()` function is used to create a range of indices to exclude from the new list. The list comprehension then filters out the elements at those indices and returns a new list containing the remaining elements.

Finally, the function uses the `print()` function to output the modified `new_list` to the console.

Overall, this code demonstrates how to use a list comprehension and the `enumerate()` function to remove several elements from a list of integers in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/remove_several_numbers_from_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[12, 88, 120, 155]
```

At this point, your code is running successfully!
