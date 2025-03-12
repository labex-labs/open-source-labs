# Processing the Data

Now that we've learned how to read a file, the next step is to process each line of the file to calculate the cost of each stock purchase. This is an important part of working with data in Python, as it allows us to extract meaningful information from the file.

Each line in the file follows a specific format: `[Stock Symbol] [Number of Shares] [Price per Share]`. To calculate the cost of each stock purchase, we need to extract the number of shares and the price per share from each line. Then, we multiply these two values together to get the cost of that particular stock purchase. Finally, we add this cost to our running total to find the overall cost of the portfolio.

Let's modify the `portfolio_cost()` function in the `pcost.py` file to achieve this. Here's the modified code:

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

Let's break down what this modified function does step by step:

1. **Strips whitespace**: We use the `strip()` method to remove any leading or trailing whitespace from each line. This ensures that we don't accidentally include extra spaces when we split the line into fields.
2. **Skips empty lines**: If a line is empty (i.e., it contains only whitespace), we use the `continue` statement to skip it. This helps us avoid errors when trying to split an empty line.
3. **Splits the line into fields**: We use the `split()` method to split each line into a list of fields based on whitespace. This allows us to access each part of the line separately.
4. **Extracts relevant data**: We extract the number of shares and the price per share from the list of fields. The number of shares is the second field, and the price per share is the third field. We convert these values to the appropriate data types (`int` for shares and `float` for price) so that we can perform arithmetic operations on them.
5. **Calculates the cost**: We multiply the number of shares by the price per share to calculate the cost of this stock purchase.
6. **Adds to the total**: We add the cost of this stock purchase to the running total cost.
7. **Prints debug information**: We print some information about each stock purchase to help us see what's happening. This includes the stock symbol, the number of shares, the price per share, and the total cost of the purchase.

Now, let's run the code to see if it works. Open your terminal and run the following command:

```bash
python3 ~/project/pcost.py
```

After running the command, you should see detailed information about each stock purchase, followed by the total cost of the portfolio. This output will help you verify that the function is working correctly and that you've calculated the total cost accurately.
