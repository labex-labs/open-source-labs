# Reading a Portfolio from a CSV File

In this step, you will create a function called `read_portfolio(filename)` that reads stock data from a CSV file and returns a list of `Stock` objects.

## Understanding CSV Files

CSV (Comma-Separated Values) files are a common format for storing tabular data. Each line represents a row of data, with columns separated by commas. The first line often contains headers that describe the data in each column.

## Implementation Instructions

1. Open the `stock.py` file in the editor if it's not already open.

2. Locate the `# TODO: Add read_portfolio(filename) function here` comment.

3. Add the following function below the comment:

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

4. Save the file by pressing `Ctrl+S` or selecting "File > Save" from the menu.

5. Create a test script called `test_portfolio.py` to verify your function:

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

6. Run the test script:

```bash
python3 test_portfolio.py
```

You should see output listing all the stocks from the portfolio.csv file:

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

This confirms that your `read_portfolio` function is correctly reading the CSV file and creating `Stock` objects from its data.
