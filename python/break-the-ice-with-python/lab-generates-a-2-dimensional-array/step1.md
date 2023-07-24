# Generates a 2 Dimensional Array

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i \_ j.

## Note

i=0,1.., X-1; j=0,1.., Y-1.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generates_a_2_dimensional_array.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def generates_a_2_dimensional_array():
    x, y = map(int, input().split(','))
    lst = [[i*j for j in range(y)] for i in range(x)]
    print(lst)


generates_a_2_dimensional_array()

```

This Python code defines a function called `generates_a_2_dimensional_array`. Within the function, the user is prompted to input two integers separated by a comma.

The `map` is used to convert the input string into two integers, which are assigned to the variables `x` and `y`.

A 2-dimensional list is then generated using a nested list comprehension. The outer list comprehension iterates over the range of `x`, and the inner list comprehension iterates over the range of `y`. For each pair of indices `(i, j)`, the value of `i*j` is computed and added to the inner list.

The resulting 2-dimensional list is stored in the variable `lst`.

Finally, the resulting 2-dimensional list is printed to the console using the `print` function.

Overall, this code demonstrates how to use a nested list comprehension in Python to generate a 2-dimensional list, and how to use the `map` function to convert user input into integers.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generates_a_2_dimensional_array.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
3,5
```

Then, the output of the program should be:

```bash
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```

At this point, your code is running successfully!
