# Processing the Data and Calculating the Cost

Now that we can read the file, let's update our code to process each line and calculate the total cost of the portfolio.

## Update the Program

Open the `pcost.py` file again:

```bash
nano ~/project/pcost.py
```

Update the `portfolio_cost` function to process each line and calculate the cost:

```python
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
            # Split the line into fields
            fields = line.split()

            # Ensure we have enough fields
            if len(fields) >= 3:
                # The stock symbol is fields[0] (we don't use it here)
                # The share quantity is fields[1]
                # The price per share is fields[2]
                try:
                    shares = int(fields[1])
                    price = float(fields[2])
                    total_cost += shares * price
                    print(f"Added {shares} shares of {fields[0]} at ${price:.2f} per share")
                except ValueError:
                    print(f"Couldn't parse line: {line.strip()}")

    return total_cost
```

In this updated code:

1. We split each line into fields using the `split()` method, which divides the string at whitespace by default.
2. We check if there are at least 3 fields (symbol, shares, price).
3. We convert the shares to an integer and the price to a float.
4. We calculate the cost of this line (shares \* price) and add it to the running total.
5. We use a try-except block to handle any lines that might have invalid data.

Save the file by pressing `Ctrl+O`, then `Enter`, and exit the editor with `Ctrl+X`.

## Testing the Updated Program

Let's test our updated program:

```bash
python3 ~/project/pcost.py
```

You should now see output showing the processing of each line and the calculated cost for each stock:

```
Added 100 shares of AA at $32.20 per share
Added 50 shares of IBM at $91.10 per share
Added 150 shares of CAT at $83.44 per share
Added 200 shares of MSFT at $51.23 per share
Added 95 shares of GE at $40.37 per share
Added 50 shares of MSFT at $65.10 per share
Added 100 shares of IBM at $70.44 per share
Total cost: $44671.15
```

The program now calculates the total cost of the portfolio. Let's finalize it in the next step.
