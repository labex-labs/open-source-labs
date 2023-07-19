# Remove Duplicate Numbers from List

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/remove_duplicate_numbers_from_list.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def remove_duplicate_numbers_from_list():
    li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    for i in li:
        if li.count(i) > 1:
            li.remove(i)
    print(li)


remove_duplicate_numbers_from_list()

```

This Python code defines a function called `remove_duplicate_numbers_from_list` that removes duplicate numbers from a list of integers. The function creates a list called `li` containing the integers `[12, 24, 35, 24, 88, 120, 155, 88, 120, 155]`, some of which are duplicates.

The function then uses a `for` loop to iterate over each element in `li`. For each element, it uses the `count()` method to determine how many times that element appears in the list. If the element appears more than once, the function uses the `remove()` method to delete one instance of that element. This loop continues until there are no more duplicate elements in the list.

Finally, the function uses the `print()` function to output the modified `li` list to the console.

It's important to note that this code can only remove one instance of a duplicate element at a time, because the `remove()` method only removes one instance per call. If there are multiple duplicate elements in the list, this function will only remove one of them.

Overall, this code demonstrates how to use the `count()` and `remove()` methods to remove duplicate elements from a list of integers in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/remove_duplicate_numbers_from_list.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[12, 35, 24, 88, 120, 155]
```

At this point, your code is running successfully!
