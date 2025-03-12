# Finalizing the Program

Now let's clean up our code and make the final version of `pcost.py`.

We'll remove the debug print statements and ensure the final output is formatted nicely:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    try:
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

                # Calculate the cost of this stock purchase and add to the total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Return the total cost
    return total_cost

# Main block to run when the script is executed directly
if __name__ == '__main__':
    # Call the function with the portfolio file
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

This final version adds:

1. Error handling to catch file not found and other exceptions
2. A proper formatting of the total cost to two decimal places
3. A `__name__ == '__main__'` check to ensure the code only runs when the script is executed directly

Run the final code:

```bash
python3 ~/project/pcost.py
```

You should see the total cost of the portfolio, which should be $44671.15.

Congratulations! You've successfully created a Python program that reads data from a file, processes it, and calculates a result.
