# Adding Error Handling

When you're working with real - world data, it's very common to come across inconsistencies or errors. For example, the data might have missing values, incorrect formats, or other issues. Python offers exception handling mechanisms to deal with these situations gracefully. Exception handling allows your program to continue running even when it encounters an error, instead of crashing abruptly.

## Understanding the Problem

Let's take a look at the `portfolio3.dat` file. This file contains some data about a portfolio, like the stock symbol, the number of shares, and the price per share. To view the contents of this file, we can use the following command:

```bash
cat /home/labex/project/portfolio3.dat
```

When you run this command, you'll notice that some lines in the file have dashes (`-`) instead of numbers for the shares. Here's an example of what you might see:

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

If we try to run our current code on this file, it will crash. The reason is that our code expects to convert the number of shares into an integer, but it can't convert a dash (`-`) into an integer. Let's try running the code and see what happens:

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

You'll see an error message like this:

```
ValueError: invalid literal for int() with base 10: '-'
```

This error occurs because Python can't convert the `-` character to an integer when it tries to execute `int(fields[1])`.

## Introduction to Exception Handling

Python's exception handling uses `try` and `except` blocks. The `try` block contains the code that might raise an exception. An exception is an error that occurs during the execution of a program. The `except` block contains the code that will be executed if an exception occurs in the `try` block.

Here's an example of how `try` and `except` blocks work:

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
```

When Python executes the code in the `try` block, if an exception occurs, the execution immediately jumps to the matching `except` block. The `ExceptionType` in the `except` block specifies the type of exception that we want to handle. The variable `e` contains information about the exception, such as the error message.

## Modifying the Function with Exception Handling

Let's update our `pcost.py` file to handle errors in the data. We'll use the `try` and `except` blocks to skip the lines with bad data and show a warning message.

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    Handles lines with bad data by skipping them and showing a warning.

    Args:
        filename: The name of the portfolio file

    Returns:
        The total cost of the portfolio as a float
    """
    total_cost = 0.0

    # Open the file and read through each line
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                # Extract the data (symbol, shares, price)
                shares = int(fields[1])
                price = float(fields[2])
                # Add the cost to our running total
                total_cost += shares * price
            except ValueError as e:
                # Print a warning for lines that can't be parsed
                print(f"Couldn't parse: '{line}'")
                print(f"Reason: {e}")

    return total_cost

# Call the function with the portfolio3.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

In this updated code, we first open the file and read it line by line. For each line, we split it into fields. Then, we try to convert the number of shares to an integer and the price to a float. If this conversion fails (i.e., a `ValueError` occurs), we print a warning message and skip that line. Otherwise, we calculate the cost of the shares and add it to the total cost.

## Testing the Updated Function

Now let's run the updated program with the problematic file. First, we need to navigate to the project directory, and then we can run the Python script.

```bash
cd /home/labex/project
python3 pcost.py
```

You should see output like this:

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

The program now does the following:

1. It attempts to process each line of the file.
2. If a line contains invalid data, it catches the `ValueError`.
3. It prints a helpful message about the problem.
4. It continues processing the rest of the file.
5. It returns the total cost based on the valid lines.

This approach makes our program much more robust when dealing with imperfect data. It can handle errors gracefully and still provide useful results.
