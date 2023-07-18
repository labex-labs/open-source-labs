# Print Even Numbers

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_even_numbers.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def even_generator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input())
values = []
for i in even_generator(n):
    values.append(str(i))

print(",".join(values))

```

This Python code defines a function called `even_generator` that takes an integer `n` as input. The function uses a `while` loop to generate even numbers from 0 to `n` using a generator.

Within the `while` loop, an `if` statement is used to check if the current value of `i` is even. If it is, the `yield` keyword is used to return the value of `i` as the next element of the generator.

The `i` variable is then incremented by 1.

In the main program, the user is prompted to enter an integer value for `n`.

An empty list `values` is then created.

A `for` loop is used to iterate over the elements of the generator returned by the `even_generator` function. Within the loop, each even number is appended to the `values` list as a string.

Finally, the elements of the `values` list are joined together using the `join` method with the `,` character as the separator, and the resulting string is printed to the console using the `print` function.

Overall, this code demonstrates how to use generators in Python to generate a sequence of even numbers, and how to use a `for` loop to iterate over the elements of the generator and append them to a list.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_even_numbers.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following n is given as input to the program:

```bash
10
```

Then, the output of the program should be:

```bash
0,2,4,6,8,10
```

At this point, your code is running successfully!
