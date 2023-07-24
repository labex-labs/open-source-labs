# Recursive Summation

Given a number N. Find sum of 1 to N using recursion.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/recursive_summation.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def rec(n):
    if n == 0:
        return n
    return rec(n-1) + n


n = int(input())
sum = rec(n)
print(sum)

```

This Python code defines a recursive function called `rec` that takes an integer `n` as input. Within the function, an `if` statement is used to check if `n` is equal `0`. If `n` is `0`, the function returns `0`. Otherwise, the function calls itself recursively with the argument `n-1` and adds `n` to the result.

The recursive call to `rec(n-1)` means that the function will call itself repeatedly with decreasing values of `n` until it reaches the base case of `n=0`. At that point, the function will start returning values and the recursive calls will start to unwind.

The main part of the code prompts the user to enter an integer `n`, which is read using the `input` function and converted to an integer using the `int` function. The resulting integer is then passed as an argument to the `rec` function, and the resulting value is stored in the variable `sum`.

Finally, the value of `sum` is printed to the console using the `print` function.

Overall, this code demonstrates how to use recursion in Python to define a function that calculates a value based on a recursive formula. In this case, the function calculates the sum of integers from `0` to `n`.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/recursive_summation.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following N is given as input to the program:

```bash
5
```

Then, the output of the program should be:

```bash
15
```

At this point, your code is running successfully!
