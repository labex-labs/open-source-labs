# Print the Last 5 Elements

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_the_last_5_elements.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_the_last_5_elements():
    li = list()
    for i in range(1, 21):
        li.append(i**2)
    print(li[-5:])


print_the_last_5_elements()

```

This Python code defines a function called `print_the_last_5_elements`. Within the function, an empty list `li` is created using the `list` function.

A `for` loop is then used to iterate over the integers from `1` to `20`. Within the loop, the square of each integer is calculated using the expression `i**2`, and the resulting value is appended to the list `li` using the `append` method.

After the loop completes, the `print` function is used to print the last five elements of the list `li` using slicing. The syntax `li[-5:]` returns a new list containing the last five elements of `li`.

Overall, this code demonstrates how to use a `for` loop and the `append` method to create a list of the squares of the integers from `1` to `20`, and print the last five elements of the list using slicing.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_the_last_5_elements.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[256, 289, 324, 361, 400]
```

At this point, your code is running successfully!
