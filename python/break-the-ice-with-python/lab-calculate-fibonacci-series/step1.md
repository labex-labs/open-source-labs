# Calculate Fibonacci Series

The Fibonacci Sequence is computed based on the following formula:

```bash
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```

Please write a program to compute the value of f(n) with a given n input by console.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculate_fibonacci_series.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def f(n):
    if n < 2:
        return n
    return f(n-1) + f(n-2)


n = int(input())
print(f(n))

```

This Python code implements a recursive function to calculate the value of the nth number in the Fibonacci sequence. It takes user input to determine the value of `n` and uses recursive calls to calculate the sum of the first two numbers. If `n` is less than 2, it returns `n` itself; otherwise, it returns the sum of the (n-1)th and (n-2)th numbers. Finally, the return value of the function is printed to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculate_fibonacci_series.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following n is given as input to the program:

```bash
7
```

Then, the output of the program should be:

```bash
13
```

At this point, your code is running successfully!
