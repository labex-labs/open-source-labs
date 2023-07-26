# Define Anonymous Functions

Write a program which can `map()` to make a list whose elements are square of elements in `[1,2,3,4,5,6,7,8,9,10]`.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/define_anonymous_functions.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def define_anonymous_functions():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
    print(list(squaredNumbers))               # converting the object into list


define_anonymous_functions()

```

This Python code defines a function called `define_anonymous_functions`. Within the function, a list of integers called `li` is defined.

The `map` function is then used to apply an anonymous function to each element of the list. The anonymous function is defined using the `lambda` keyword and takes a single parameter `x`. The function returns the square of `x`.

The `map` function returns a map object, which is an iterable that contains the results of applying the anonymous function to each element of the list. To convert the map object into a list, the `list` function is used.

Finally, the resulting list of squared numbers is printed to the console using the `print` function.

Overall, this code demonstrates how to use anonymous functions in Python to apply a function to each element of a list using the `map` function. It also shows how to convert a map object into a list using the `list` function.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/define_anonymous_functions.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

At this point, your code is running successfully!
