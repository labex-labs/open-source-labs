# Defining a Function

In this step, you will learn how to create a function that reads portfolio data from a file and calculates the total cost.

## Understanding the Problem

In the previous lab, you may have written code that reads portfolio data and calculates the total cost. Let's convert that code into a reusable function.

The portfolio data files contain information in the format:

```
Symbol Shares Price
```

For example, in `portfolio.dat`:

```
AA 100 32.20
IBM 50 91.10
...
```

Each line represents a stock holding with:

- Stock symbol (e.g., AA)
- Number of shares (e.g., 100)
- Price per share (e.g., 32.20)

## Creating the Function

Let's create a Python file called `pcost.py` in the `/home/labex/project` directory with the following code:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file

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
            # Extract the data (symbol, shares, price)
            shares = int(fields[1])
            price = float(fields[2])
            # Add the cost to our running total
            total_cost += shares * price

    return total_cost

# Call the function with the portfolio.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

## Testing the Function

Now, let's run the program to see if it works:

```bash
cd /home/labex/project
python3 pcost.py
```

You should see the output:

```
44671.15
```

This is the total cost of all the stocks in the portfolio.

## Understanding the Code

Let's break down what our function does:

1. Takes a filename as an input parameter
2. Opens the file and reads it line by line
3. For each line, splits it into fields using the `split()` method
4. Converts the number of shares to an integer and the price to a float
5. Calculates the cost (shares \* price) and adds it to the running total
6. Returns the final total cost

This function is now reusable - we can call it with different portfolio files to calculate their costs.
