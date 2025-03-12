# Creating Your Own Module

Now that you understand how to use existing modules, let's create a new module from scratch.

## Creating a Report Module

Let's create a simple module for generating stock reports:

1. Create a new file named `report.py`:

```bash
cd ~/project
nano report.py
```

2. Add the following code to the file:

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

This module includes:

- A function to read a portfolio file
- A function to print a formatted report
- A main block that runs when the file is executed directly

3. Save and exit the editor (Ctrl+O, Enter, then Ctrl+X).

## Testing Your Module

Let's test our new module:

1. Run the script directly:

```bash
python3 report.py
```

You should see a formatted report showing the portfolio stocks and their values:

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. Now, use the module from the Python interpreter:

```bash
python3
```

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

You should see:

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. Use the imported module to calculate the total cost yourself:

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

The output should be `44671.15`.

4. Create a custom report for a specific stock type:

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

This should print a report showing only the IBM stocks:

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. Exit the Python interpreter:

```python
exit()
```

You've now successfully created and used your own Python module, combining both functions and a main block that only runs when the file is executed directly.
