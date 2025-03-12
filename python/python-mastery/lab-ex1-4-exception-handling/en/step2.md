# Adding Error Handling

When working with real-world data, you often encounter inconsistencies or errors. Python provides exception handling mechanisms to deal with these situations gracefully.

## Understanding the Problem

Let's examine the `portfolio3.dat` file:

```bash
cat /home/labex/project/portfolio3.dat
```

You'll notice some lines have dashes (`-`) instead of numbers for the shares:

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

If we try to run our current code on this file, it will crash:

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

You'll see an error like:

```
ValueError: invalid literal for int() with base 10: '-'
```

This happens because Python can't convert the `-` character to an integer when it tries to execute `int(fields[1])`.

## Introduction to Exception Handling

Python's exception handling uses `try` and `except` blocks:

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
```

When Python executes the code in the `try` block, if an exception occurs, the execution immediately jumps to the matching `except` block.

## Modifying the Function with Exception Handling

Let's update our `pcost.py` file to handle errors in the data:

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

## Testing the Updated Function

Now let's run the updated program with the problematic file:

```bash
cd /home/labex/project
python3 pcost.py
```

You should see output like:

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

The program now:

1. Attempts to process each line of the file
2. If a line contains invalid data, it catches the ValueError
3. Prints a helpful message about the problem
4. Continues processing the rest of the file
5. Returns the total cost based on the valid lines

This approach makes our program much more robust when dealing with imperfect data.
