# Square each Odd Number

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/square_each_odd_number.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def square_each_odd_number():
    seq = input().split(',')
    lst = [int(i) for i in seq]

    def flt(i):  # Define a filter function
        return i % 2 != 0

    result_l = [str(i * i) for i in filter(flt, lst)]
    print(",".join(result_l))


square_each_odd_number()

```

This Python code defines a function called `square_each_odd_number()` that squares each odd number in a list of integers. The function prompts the user to input a series of comma-separated values that will be used to create a list of integers.

The function creates a list called `lst` by converting the input values to integers using a list comprehension.

The function then defines a filter function called `flt()` that returns `True` for odd numbers and `False` for even numbers.

The function uses the `filter()` function to apply the `flt()` filter function to the `lst` list and create a new list called `result_l` that contains the squares of each odd number in the `lst` list. The `map()` function is used to apply the `square()` function to each odd number in the filtered list.

Finally, the function uses the `join()` method to concatenate the elements in the `result_l` list into a single string separated by commas, and uses the `print()` function to output the resulting string to the console.

Overall, this code demonstrates how to use a filter function and a list comprehension to square each odd number in a list of integers in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/square_each_odd_number.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
1,2,3,4,5,6,7,8,9
```

Then, the output of the program should be:

```bash
1,9,25,49,81
```

At this point, your code is running successfully!
