# Exercise 3.1: Structuring a program as a collection of functions

Modify your `report.py` program so that all major operations, including calculations and output, are carried out by a collection of functions. Specifically:

- Create a function `print_report(report)` that prints out the report.
- Change the last part of the program so that it is nothing more than a series of function calls and no other computation.

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


def calculate_performance(portfolio):
    """
    Calculate the performance of the stocks in the portfolio.
    """
    for stock in portfolio:
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


def main():
    portfolio = read_portfolio("/home/labex/project/portfolio.csv")
    portfolio = calculate_performance(portfolio)
    print_report(portfolio)


if __name__ == "__main__":
    main()
```