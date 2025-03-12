# Reading a Portfolio from a CSV File

In this step, we're going to create a function that reads stock data from a CSV file and returns a list of `Stock` objects. A `Stock` object represents a stock holding, and by the end of this step, you'll be able to read a portfolio of stocks from a CSV file.

## Understanding CSV Files

CSV, which stands for Comma-Separated Values, is a very common format for storing tabular data. Think of it like a simple spreadsheet. Each line in a CSV file represents a row of data, and the columns within that row are separated by commas. Usually, the first line of a CSV file contains headers. These headers describe what kind of data is in each column. For example, in a stock portfolio CSV, the headers might be "Name", "Shares", and "Price".

## Implementation Instructions

1. First, open the `stock.py` file in your code editor. If it's already open, that's great! If not, find it and open it up. This is where we'll be adding our new function.

2. Once the `stock.py` file is open, look for the comment `# TODO: Add read_portfolio(filename) function here`. This comment is a placeholder that tells us where to put our new function.

3. Below that comment, add the following function. This function is called `read_portfolio`, and it takes a filename as an argument. The purpose of this function is to read the CSV file, extract the stock data, and create a list of `Stock` objects.

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

Let's break down what this function does. First, it creates an empty list called `portfolio`. Then, it opens the CSV file in read mode. The `next(f)` statement skips the first line, which is the header line. After that, it loops through each line in the file. For each line, it splits the line into a list of values, extracts the name, number of shares, and price, creates a `Stock` object, and adds it to the `portfolio` list. Finally, it returns the `portfolio` list.

4. After adding the function, save the `stock.py` file. You can do this by pressing `Ctrl+S` on your keyboard or by selecting "File > Save" from the menu in your code editor. Saving the file ensures that your changes are preserved.

5. Now, we need to test our `read_portfolio` function. Create a new Python script called `test_portfolio.py`. This script will import the `read_portfolio` function from the `stock.py` file, read the portfolio from a CSV file, and print information about each stock in the portfolio.

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

In this script, we first import the `read_portfolio` function. Then, we call the function with the filename `portfolio.csv` to get the list of `Stock` objects. After that, we loop through the list and print information about each stock. Finally, we print the total number of stocks in the portfolio.

6. To run the test script, open your terminal or command prompt, navigate to the directory where the `test_portfolio.py` file is located, and run the following command:

```bash
python3 test_portfolio.py
```

If everything is working correctly, you should see output that lists all the stocks from the `portfolio.csv` file, along with their names, number of shares, and prices. You should also see the total number of stocks in the portfolio.

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $70.44

Total number of stocks in portfolio: 7
```

This output confirms that your `read_portfolio` function is correctly reading the CSV file and creating `Stock` objects from its data.
