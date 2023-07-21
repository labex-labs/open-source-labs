# Get a Tuple of Even Elements

Write a program to generate and print another tuple whose values are even numbers in the given tuple `(1,2,3,4,5,6,7,8,9,10)`.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/get_a_tuple_of_even_elements.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def get_a_tuple_of_even_elements():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tpl1 = tuple(i for i in tpl if i % 2 == 0)
    print(tpl1)


get_a_tuple_of_even_elements()

```

This Python code defines a function called `get_a_tuple_of_even_elements`. Within the function, a tuple `tpl` is defined with ten elements.

A new tuple `tpl1` is then generated using a tuple comprehension. The tuple comprehension iterates over the elements of `tpl` and includes only the even elements in the new tuple.

The resulting tuple of even elements is stored in the variable `tpl1`.

Finally, the resulting tuple is printed to the console using the `print` function.

Overall, this code demonstrates how to use a tuple comprehension in Python to generate a new tuple with only the even elements of an existing tuple.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/get_a_tuple_of_even_elements.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
(2, 4, 6, 8, 10)
```

At this point, your code is running successfully!
