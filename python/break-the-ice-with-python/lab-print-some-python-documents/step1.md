# Print some Python Documents

Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as `str()`, `sorted()`, `input()`.

And add document for your own function.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_some_python_documents.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
print(str.__doc__)
print('----------------------------------------------------------------------')
print(sorted.__doc__)
print('----------------------------------------------------------------------')
print(input.__doc__)
print('----------------------------------------------------------------------')

def pow(n, p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p


print(pow(3, 4))
print(pow.__doc__)

```

This Python code demonstrates the use of docstrings in Python.

The first three `print` statements use the `__doc__` attribute to print the docstrings of the built-in functions `str`, `sorted`, and `input`, respectively.

The `__doc__` attribute is a special attribute of Python objects that contains the docstring of the object. A docstring is a string literal that appears as the first statement in a module, function, class, or method definition. It is used to document the purpose, usage, and behavior of the object.

The fourth part of the code defines a function called `pow` that takes two parameters `n` and `p` and returns the value of `n` raised to the power of `p`.

The function includes a docstring that describes the purpose, parameters, and return value of the function.

The `print` statement at the end of the code calls the `pow` function with arguments `3` and `4` and prints the result to the console. It also prints the docstring of the `pow` function using the `__doc__` attribute.

Overall, this code demonstrates how to use docstrings in Python to document the purpose, usage, and behavior of functions and other objects.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_some_python_documents.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, output the symmetric difference integers in ascending order, one per line.

```bash
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
----------------------------------------------------------------------
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.
----------------------------------------------------------------------
Read a string from standard input.  The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
On *nix systems, readline is used if available.
----------------------------------------------------------------------
81

    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p

```

At this point, your code is running successfully!
