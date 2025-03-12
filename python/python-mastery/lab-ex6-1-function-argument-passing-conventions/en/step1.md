# Understanding Function Argument Passing

In Python, functions are a fundamental concept that allows you to group a set of statements together to perform a specific task. When you call a function, you often need to provide it with some data, which we call arguments. Python offers different ways to pass these arguments to functions. This flexibility is incredibly useful as it helps you write cleaner and more maintainable code. Before we start applying these techniques to our project, let's take a closer look at these argument passing conventions.

## Creating a Backup of Your Work

Before we start making changes to our `stock.py` file, it's a good practice to create a backup. This way, if something goes wrong during our experimentation, we can always go back to the original version. To create a backup, open a terminal and run the following command:

```bash
cp stock.py orig_stock.py
```

This command uses the `cp` (copy) command in the terminal. It takes the `stock.py` file and creates a copy of it named `orig_stock.py`. By doing this, we ensure that our original work is safely preserved.

## Exploring Function Argument Passing

In Python, there are several ways to call functions with different types of arguments. Let's explore each of these methods in detail.

### 1. Positional Arguments

The simplest way to pass arguments to a function is by position. When you define a function, you specify a list of parameters. When you call the function, you provide values for these parameters in the same order as they are defined.

Here's an example:

```python
def calculate(x, y, z):
    return x + y + z

# Call with positional arguments
result = calculate(1, 2, 3)
print(result)  # Output: 6
```

In this example, the `calculate` function takes three parameters: `x`, `y`, and `z`. When we call the function with `calculate(1, 2, 3)`, the value `1` is assigned to `x`, `2` is assigned to `y`, and `3` is assigned to `z`. The function then adds these values together and returns the result.

### 2. Keyword Arguments

In addition to positional arguments, you can also specify arguments by their names. This is called using keyword arguments. When you use keyword arguments, you don't have to worry about the order of the arguments.

Here's an example:

```python
# Call with a mix of positional and keyword arguments
result = calculate(1, z=3, y=2)
print(result)  # Output: 6
```

In this example, we first pass the positional argument `1` for `x`. Then, we use keyword arguments to specify the values for `y` and `z`. The order of the keyword arguments doesn't matter, as long as you provide the correct names.

### 3. Unpacking Sequences and Dictionaries

Python provides a convenient way to pass sequences and dictionaries as arguments using the `*` and `**` syntax. This is called unpacking.

Here's an example of unpacking a tuple into positional arguments:

```python
# Unpacking a tuple into positional arguments
args = (1, 2, 3)
result = calculate(*args)
print(result)  # Output: 6
```

In this example, we have a tuple `args` that contains the values `1`, `2`, and `3`. When we use the `*` operator before `args` in the function call, Python unpacks the tuple and passes its elements as positional arguments to the `calculate` function.

Here's an example of unpacking a dictionary into keyword arguments:

```python
# Unpacking a dictionary into keyword arguments
kwargs = {'y': 2, 'z': 3}
result = calculate(1, **kwargs)
print(result)  # Output: 6
```

In this example, we have a dictionary `kwargs` that contains the key-value pairs `'y': 2` and `'z': 3`. When we use the `**` operator before `kwargs` in the function call, Python unpacks the dictionary and passes its key-value pairs as keyword arguments to the `calculate` function.

### 4. Accepting Variable Arguments

Sometimes, you may want to define a function that can accept any number of arguments. Python allows you to do this using the `*` and `**` syntax in the function definition.

Here's an example of a function that accepts any number of positional arguments:

```python
# Accept any number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

In this example, the `sum_all` function uses the `*args` parameter to accept any number of positional arguments. The `*` operator collects all the positional arguments into a tuple named `args`. The function then uses the built-in `sum` function to add up all the elements in the tuple.

Here's an example of a function that accepts any number of keyword arguments:

```python
# Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Python", year=1991)
# Output:
# name: Python
# year: 1991
```

In this example, the `print_info` function uses the `**kwargs` parameter to accept any number of keyword arguments. The `**` operator collects all the keyword arguments into a dictionary named `kwargs`. The function then iterates over the key-value pairs in the dictionary and prints them.

These techniques will help us create more flexible and reusable code structures in the following steps. To get more comfortable with these concepts, let's open the Python interpreter and try some of these examples.

```bash
python3
```

Once you're in the Python interpreter, try entering the examples above. This will give you hands-on experience with these argument passing techniques.
