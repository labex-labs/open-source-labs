# Recursive Functions

Write a program to compute:

```bash
f(n)=f(n-1)+100 when n>0
and f(0)=0
```

With a given n input by console (n>0).

## Preparation

Before we start writing the code, we should open the `/home/labex/project/recursive_functions.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100


n = int(input())
print(f(n))

```

This Python code defines a recursive function called `f` that takes an integer `n` as input. Within the function, an `if` statement is used to check if `n` is equal to `0`. If `n` is `0`, the function returns `0`. Otherwise, the function calls itself recursively with the argument `n-1` and adds `100` to the result.

The recursive call to `f(n-1)` means that the function will call itself repeatedly with decreasing values of `n` until it reaches the base case of `n=0`. At that point, the function will start returning values and the recursive calls will start to unwind.

The main part of the code prompts the user to enter an integer `n`, which is read using the `input` function and converted to an integer using the `int` function. The resulting integer is then passed as an argument to the `f` function, and the resulting value is printed to the console using the `print` function.

Overall, this code demonstrates how to use recursion in Python to define a function that calculates a value based on a recursive formula. In this case, the function calculates the sum of `100` for `n` times, starting from `0`.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/recursive_functions.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following n is given as input to the program:

```bash
5
```

Then, the output of the program should be:

```bash
500
```

At this point, your code is running successfully!
