# Opening and Reading the Portfolio File

In this step, we will write the code to open and read the portfolio data file.

## Create the Python Program

Open the file `pcost.py` using the `nano` text editor:

```bash
nano ~/project/pcost.py
```

## Writing the Basic File Reading Code

Let's start by writing the code to open and read the file. Enter the following Python code in the editor:

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

    # Open the file and read each line
    with open(filename, 'r') as file:
        for line in file:
            print(f"Processing line: {line.strip()}")

    return total_cost

# Calculate the portfolio cost
if __name__ == '__main__':
    cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${cost}')
```

In this code:

1. We define a function `portfolio_cost` that takes a filename as input.
2. We initialize a variable `total_cost` to store the running sum.
3. We open the file using a `with` statement, which ensures the file is properly closed when we're done.
4. We iterate through each line of the file, printing each line for now.
5. The `if __name__ == '__main__'` block allows the script to be used both as a standalone program and as an importable module.

Save the file by pressing `Ctrl+O`, then `Enter`, and exit the editor with `Ctrl+X`.

## Testing the File Reading

Let's test our program to see if it correctly reads the file:

```bash
python3 ~/project/pcost.py
```

You should see output similar to this:

```
Processing line: AA 100 32.20
Processing line: IBM 50 91.10
Processing line: CAT 150 83.44
Processing line: MSFT 200 51.23
Processing line: GE 95 40.37
Processing line: MSFT 50 65.10
Processing line: IBM 100 70.44
Total cost: $0.0
```

Great! Our program is successfully reading the file line by line. In the next step, we will add the code to process each line and calculate the total cost.
