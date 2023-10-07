# pcost_2.15.py

import csv


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                shares = int(row[1])
                price = float(row[2])
                cost = shares * price
                total_cost += cost
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")
    return total_cost


cost = portfolio_cost("/home/labex/project/missing.csv")
