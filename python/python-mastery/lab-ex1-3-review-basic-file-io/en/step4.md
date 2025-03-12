# Finalizing the Program

Let's finalize our program by making it more user-friendly and adding error handling for the file operations.

## Improve the Program

Open the `pcost.py` file one last time:

```bash
nano ~/project/pcost.py
```

Update the entire program with the following code:

```python
# pcost.py
#
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Calculate the total cost of a portfolio of stocks.

    Args:
        filename: The name of the portfolio data file

    Returns:
        The total cost of the portfolio
    """
    total_cost = 0.0

    try:
        # Open the file and read each line
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                # Skip empty lines
                if not line.strip():
                    continue

                # Split the line into fields
                fields = line.split()

                # Ensure we have enough fields
                if len(fields) >= 3:
                    # The stock symbol is fields[0]
                    # The share quantity is fields[1]
                    # The price per share is fields[2]
                    try:
                        shares = int(fields[1])
                        price = float(fields[2])
                        cost = shares * price
                        total_cost += cost
                    except ValueError:
                        print(f"Line {line_num}: Couldn't parse: {line.strip()}")
                else:
                    print(f"Line {line_num}: Not enough fields: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: Could not find the file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return 0.0

    return total_cost

# Calculate the portfolio cost
if __name__ == '__main__':
    import sys

    # Use command line argument if provided, otherwise use default filename
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'portfolio.dat'

    cost = portfolio_cost(filename)
    print(f'Total cost: ${cost:.2f}')
```

In this final version:

1. We've added better error handling around file operations.
2. We've added line numbers to error messages to help identify problematic lines.
3. We now skip empty lines.
4. We've added command-line argument support, so the user can specify a different file.
5. We've formatted the output to show the cost with two decimal places.

Save the file by pressing `Ctrl+O`, then `Enter`, and exit the editor with `Ctrl+X`.

## Test the Final Program

Let's test our finalized program:

```bash
python3 ~/project/pcost.py
```

You should see the following output:

```
Total cost: $44671.15
```

The program now provides a clean, simple output showing just the total cost.

## Testing with Command-line Arguments

You can also test the program with a command-line argument:

```bash
python3 ~/project/pcost.py portfolio.dat
```

This should give the same result:

```
Total cost: $44671.15
```

Congratulations! You have successfully created a Python program that reads a data file, processes its contents, and calculates a result.
