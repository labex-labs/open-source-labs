# Processing the Data

Now that we can read the file, we need to process each line to calculate the cost of each stock purchase.

Each line in the file has the format: `[Stock Symbol] [Number of Shares] [Price per Share]`. We need to extract the number of shares and the price per share, multiply them together, and add the result to our total cost.

Let's modify the `portfolio_cost()` function in `pcost.py`:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split the line into fields
            fields = line.split()

            # Extract the relevant data
            # fields[0] is the stock symbol (which we don't need for the calculation)
            shares = int(fields[1])  # Number of shares (second field)
            price = float(fields[2])  # Price per share (third field)

            # Calculate the cost of this stock purchase
            cost = shares * price

            # Add to the total cost
            total_cost += cost

            # Print some debug information
            print(f'{fields[0]}: {shares} shares at ${price:.2f} = ${cost:.2f}')

    # Return the total cost
    return total_cost
```

This modified function:

1. Strips any whitespace from each line
2. Skips empty lines
3. Splits each line into fields using the default whitespace delimiter
4. Extracts the number of shares and price per share
5. Calculates the cost of this stock purchase
6. Adds the cost to the total
7. Prints some debug information to see what's happening

Let's run the code to see if it works:

```bash
python3 ~/project/pcost.py
```

You should now see detailed information about each stock purchase, followed by the total cost.
