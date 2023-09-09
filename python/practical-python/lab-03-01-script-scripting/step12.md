# Exercise 3.2: Creating a top-level function for program execution

Take the last part of your program and package it into a single function `portfolio_report(portfolio_filename, prices_filename)`. Have the function work so that the following function call creates the report as before:

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

In this final version, your program will be nothing more than a series of function definitions followed by a single function call to `portfolio_report()` at the very end (which executes all of the steps involved in the program).

By turning your program into a single function, it becomes easy to run it on different inputs. For example, try these statements interactively after running your program:

```python
>>> portfolio_report('portfolio2.csv', 'prices.csv')
... look at the output ...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... look at the output ...
>>>
```

Here's a solution:

```python
import csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(stock)

    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dictionary mapping names to prices.
    """
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


def calculate_performance(portfolio, prices):
    """
    Calculate the performance of the stocks in the portfolio.
    """
    for stock in portfolio:
        stock["current_price"] = prices.get(stock["name"], 0.0)
        change = stock["current_price"] - stock["price"]
        stock["change"] = change
    return portfolio


def print_report(report):
    """
    Print out the report showing the performance of the stocks.
    """
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(("-" * 10 + " ") * len(headers))
    for stock in report:
        name = stock["name"]
        shares = stock["shares"]
        price = stock["current_price"]
        change = stock["change"]
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    """
    Generate and print the stock report given portfolio and prices data files.
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    portfolio = calculate_performance(portfolio, prices)
    print_report(portfolio)


if __name__ == "__main__":
    portfolio_report("/home/labex/project/portfolio.csv", "/home/labex/project/prices.csv")
```