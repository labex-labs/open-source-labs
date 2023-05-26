# Print Half of a Tuple

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_half_of_a_tuple.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_half_of_a_tuple():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    for i in range(0, 5):
        print(tpl[i], end=' ')
    print()
    for i in range(5, 10):
        print(tpl[i], end=' ')


print_half_of_a_tuple()

```

This Python code defines a function called `print_half_of_a_tuple`. Within the function, a tuple `tpl` is initialized with a sequence of integers.

Two `for` loops are then used to print the first half and second half of the tuple, respectively.

The first `for` loop iterates over the elements of the tuple from the first element to the fifth element (exclusive). Within the loop, the `print` function is used to print each element of the tuple followed by a space character. The `end` parameter is set to `' '` to ensure that the elements are printed on the same line.

After the first `for` loop, a `print` function is called with no arguments to print a newline character and move to the next line.

The second `for` loop iterates over the elements of the tuple from the fifth element to the tenth element (exclusive). Within the loop, the `print` function is used to print each element of the tuple followed by a space character. The `end` parameter is set to `' '` to ensure that the elements are printed on the same line.

Overall, this code demonstrates how to use loops and tuple indexing in Python to print the first half and second half of a tuple on separate lines.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_half_of_a_tuple.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
1 2 3 4 5
6 7 8 9 10
```

At this point, your code is running successfully!
