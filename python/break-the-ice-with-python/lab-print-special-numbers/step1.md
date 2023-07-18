# Print Special Numbers

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_special_numbers.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def speical_numbers_generator(n):
    if n == 0:
        return
    for i in range(n+1):
        if i % 35 == 0:    # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i


n = int(input())
resp = [str(i) for i in speical_numbers_generator(n)]
print(",".join(resp))

```

This Python code defines a function called `speical_numbers_generator` that takes an integer `n` as input. The function uses a `for` loop to iterate over the integers from `0` to `n`, and yields any integer that is divisible by `35`.

The `yield` keyword is used to create a generator object that produces a sequence of values on demand. In this case, the generator produces the special numbers that are divisible by both `5` and `7`.

The `if` statement checks if the current integer `i` is divisible by `35` using the modulo operator `%`. If the condition is true, the integer `i` is yielded by the generator.

The main part of the code prompts the user to enter an integer `n`, and then calls the `speical_numbers_generator` function with `n` as the argument. The resulting generator object is converted to a list of strings using a list comprehension, and then joined into a single string using the `join` method with a comma separator.

Finally, the resulting string is printed to the console using the `print` function.

Overall, this code demonstrates how to use generators and list comprehensions in Python to generate and manipulate a sequence of special numbers that are divisible by both `5` and `7`.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_special_numbers.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following n is given as input to the program:

```bash
100
```

Then, the output of the program should be:

```bash
0,35,70
```

At this point, your code is running successfully!
