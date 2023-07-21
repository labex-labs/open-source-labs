# Remove Special Numbers from List

By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

## Preparation

Before we start writing the code, we should open the `/home/labex/project/remove_special_numbers_from_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def remove_special_numbers_from_list():
    li = [12, 24, 35, 70, 88, 120, 155]
    li = [x for x in li if x % 35 != 0]
    print(li)


remove_special_numbers_from_list()

```

This Python code defines a function called `remove_special_numbers_from_list()` that removes special numbers from a list of integers. The function creates a list called `li` containing the integers `[12, 24, 35, 70, 88, 120, 155]`.

The function then uses a list comprehension to create a new list called `li` that contains all the elements from the original list `li` except for the elements that are divisible by 35. The list comprehension filters out the elements that are divisible by 35 using the modulo operator `%`. If an element is divisible by 35, its remainder when divided by 35 will be 0, so the list comprehension excludes those elements from the new list.

Finally, the function uses the `print()` function to output the modified `li` list to the console.

Overall, this code demonstrates how to use a list comprehension and the modulo operator `%` to remove special numbers from a list of integers in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/remove_special_numbers_from_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[12, 24, 88, 120, 155]
```

At this point, your code is running successfully!
