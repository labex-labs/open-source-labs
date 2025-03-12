# Opening and Reading the File

In this step, we will learn how to open and read a file in Python.

In Python, you can open a file using the `open()` function. This function takes two arguments - the name of the file and the mode in which to open the file. For reading a file, we use the mode 'r'.

Let's add code to `pcost.py` to open and read the `portfolio.dat` file. Open the file in the editor and add the following code:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            print(line)  # Just for debugging, to see what we're reading

    # Return the total cost
    return total_cost

# Call the function with the portfolio file
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

This code does the following:

1. Defines a function `portfolio_cost()` that takes a filename as input
2. Opens the specified file in read mode
3. Reads the file line by line, printing each line (just for debugging)
4. Returns the total cost (which is currently set to 0.0)
5. Calls the function with the filename 'portfolio.dat'
6. Prints the total cost

Run this code to see what it does. You can run the Python file from the terminal:

```bash
python3 ~/project/pcost.py
```

You should see each line of the file printed, followed by the total cost (which is currently 0.0).
