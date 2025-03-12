# Understanding Function Argument Passing

In Python, functions can be called using different argument passing techniques. This flexibility allows for cleaner, more maintainable code. Let's explore these conventions before applying them to our project.

## Creating a Backup of Your Work

First, let's make a backup of your current `stock.py` file. Open a terminal and run:

```bash
cp stock.py orig_stock.py
```

This ensures your original work is preserved.

## Exploring Function Argument Passing

In Python, you can call functions using different approaches:

### 1. Positional Arguments

The most basic way to pass arguments is by position:

```python
def calculate(x, y, z):
    return x + y + z

# Call with positional arguments
result = calculate(1, 2, 3)
print(result)  # Output: 6
```

### 2. Keyword Arguments

You can also specify arguments by name:

```python
# Call with a mix of positional and keyword arguments
result = calculate(1, z=3, y=2)
print(result)  # Output: 6
```

### 3. Unpacking Sequences and Dictionaries

Python allows you to pass sequences and dictionaries as arguments using the `*` and `**` syntax:

```python
# Unpacking a tuple into positional arguments
args = (1, 2, 3)
result = calculate(*args)
print(result)  # Output: 6

# Unpacking a dictionary into keyword arguments
kwargs = {'y': 2, 'z': 3}
result = calculate(1, **kwargs)
print(result)  # Output: 6
```

### 4. Accepting Variable Arguments

Functions can be defined to accept any number of arguments:

```python
# Accept any number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Python", year=1991)
# Output:
# name: Python
# year: 1991
```

These techniques will help us create more flexible and reusable code structures in the following steps. Let's practice by opening the Python interpreter and trying some of these examples:

```bash
python3
```

Try entering the examples above in the Python interpreter to get comfortable with these concepts.
