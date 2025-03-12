# Finalizing the Program

Now, we're going to clean up our code and create the final version of the `pcost.py` program. Cleaning up the code means removing any unnecessary parts and making sure the output looks good. This is an important step in programming because it makes our code more professional and easier to understand.

We'll start by removing the debug print statements. These statements are used during development to check the values of variables and the flow of the program, but they're not needed in the final version. Then, we'll ensure that the final output is formatted nicely.

Here's the final version of the `pcost.py` code:

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

This final version of the code has several improvements:

1. Error handling: We've added code to catch two types of errors. The `FileNotFoundError` is raised when the specified file doesn't exist. If this happens, the program will print an error message and return 0.0. The `Exception` block catches any other errors that might occur while processing the file. This makes our program more robust and less likely to crash unexpectedly.
2. Proper formatting: The total cost is formatted to two decimal places using the `:.2f` format specifier in the f-string. This makes the output look more professional and easier to read.
3. `__name__ == '__main__'` check: This is a common Python idiom. It ensures that the code inside the `if` block only runs when the script is executed directly. If the script is imported as a module into another script, this code won't run. This gives us more control over how our script behaves.

Now, let's run the final code. Open your terminal and enter the following command:

```bash
python3 ~/project/pcost.py
```

When you run this command, the program will read the `portfolio.dat` file, calculate the total cost of the portfolio, and print the result. You should see the total cost of the portfolio, which should be $44671.15.

Congratulations! You've successfully created a Python program that reads data from a file, processes it, and calculates a result. This is a great achievement, and it shows that you're on your way to becoming a proficient Python programmer.
