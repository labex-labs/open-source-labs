# Creating Your Own Module

Now that you understand how to use existing modules, it's time to create a new module from scratch. A module in Python is a file containing Python definitions and statements. It allows you to organize your code into reusable and manageable pieces. By creating your own module, you can group related functions and variables together, making your code more modular and easier to maintain.

## Creating a Report Module

Let's create a simple module for generating stock reports. This module will have functions to read a portfolio file and print a formatted report of the stocks in the portfolio.

1. First, we need to create a new file named `report.py`. To do this, we'll use the command line. Navigate to the `project` directory in your home directory and create the file using the `touch` command.

```bash
cd ~/project
touch report.py
```

2. Now, open the `report.py` file in your preferred text editor and add the following code. This code defines two functions and a main block.

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

The `read_portfolio` function reads a file containing stock information and returns a list of dictionaries, where each dictionary represents a stock with keys `name`, `shares`, and `price`. The `print_report` function takes a portfolio (a list of stock dictionaries) and prints a formatted report showing the stock name, number of shares, price, and total value. The main block at the end runs when the file is executed directly. It reads the portfolio file and prints the report.

3. After adding the code, save and exit the editor.

## Testing Your Module

Let's test our new module to make sure it works as expected.

1. First, we'll run the script directly from the command line. This will execute the main block in the `report.py` file.

```bash
python3 report.py
```

You should see a formatted report showing the portfolio stocks and their values. This report includes the stock name, number of shares, price, and total value, as well as the total value of the entire portfolio.

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

2. Next, we'll use the module from the Python interpreter. Start the Python interpreter by running the `python3` command in the terminal.

```bash
python3
```

Once the interpreter is running, we can import the `report` module and use its functions.

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

The `import report` statement makes the functions and variables defined in the `report.py` file available in the current Python session. We then use the `read_portfolio` function to read the portfolio file and store the result in the `portfolio` variable. The `len(portfolio)` statement returns the number of stocks in the portfolio, and `portfolio[0]` returns the first stock in the portfolio.

You should see the following output:

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. Now, let's use the imported module to calculate the total cost of the portfolio ourselves. We'll iterate over the stocks in the portfolio and sum up the total value of each stock.

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

The output should be `44671.15`, which is the same as the total value printed by the `print_report` function.

4. Finally, let's create a custom report for a specific stock type. We'll filter the portfolio to include only the IBM stocks and then use the `print_report` function to print a report for those stocks.

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

This should print a report showing only the IBM stocks and their values.

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. When you're done testing, exit the Python interpreter by running the `exit()` command.

```python
exit()
```

You've now successfully created and used your own Python module, combining both functions and a main block that only runs when the file is executed directly. This modular approach to programming allows you to reuse code and make your projects more organized and maintainable.
