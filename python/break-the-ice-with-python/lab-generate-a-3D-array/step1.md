# Generate a 3d Array

By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_a_3D_array.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def generate_a_3D_array():
    array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
    print(array)


generate_a_3D_array()

```

This Python code defines a function called `generate_a_3D_array`. Within the function, a 3D array is created using a nested list comprehension.

The outermost list comprehension creates a list with three elements, representing the three dimensions of the 3D array. Each element is a list created by the second list comprehension, which creates a list with five elements representing the second dimension of the 3D array. Finally, each of these five elements is a list created by the innermost list comprehension, which creates a list with eight elements representing the third dimension of the 3D array.

The `0` value is used to initialize each element of the 3D array.

Finally, the resulting 3D array is printed to the console using the `print` function.

Overall, this code demonstrates how to use nested list comprehensions in Python to create a 3D array with a specific size and initialize its elements to a specific value.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_a_3D_array.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The output of the program should be:

```bash
[[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
 [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
 [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]]
```

At this point, your code is running successfully!
