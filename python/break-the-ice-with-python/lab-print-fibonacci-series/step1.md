# Print Fibonacci Series

The Fibonacci Sequence is computed based on the following formula:

```bash
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```

Please write a program to compute and print the value of f(n) with a given n input by console.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_fibonacci_series.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]


n = int(input())
fibo = [0]*(n+1)  # initialize a list of size (n+1)
f(n)              # call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo]   # converting integer data to string type
ans = ", ".join(fibo)    # joining all string element of fibo with ',' character
print(ans)

```

This Python code defines a function called `f` that takes an integer `n` as input. The function uses recursion to calculate the `n`th Fibonacci number and stores the result in a list called `fibo`.

If `n` is less than 2, the function sets the value of `fibo[n]` to `n` and returns `n`.

Otherwise, the function recursively calls itself with `n-1` and `n-2` as arguments, and adds the results together to obtain the `n`th Fibonacci number. The result is then stored in `fibo]` and returned.

In the main program, the user is prompted to enter an integer value for `n`.

An empty list `fibo` is then created with a length of `n+1`.

The `f` function is called with `n` as the argument, which calculates and stores the Fibonacci numbers from 0 to `n` in the `fibo` list.

The elements of the `fibo` list are then converted to strings using a list comprehension.

The `join` method is then used to concatenate the elements of the `fibo` list into a single string with `,` as the separator.

Finally, the resulting string is printed to the console using the `print` function.

Overall, this code demonstrates how to use recursion and list manipulation in Python to calculate and print the Fibonacci sequence up to a given number.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_fibonacci_series.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following n is given as input to the program:

```bash
7
```

Then, the output of the program should be:

```bash
0, 1, 1, 2, 3, 5, 8, 13
```

At this point, your code is running successfully!
