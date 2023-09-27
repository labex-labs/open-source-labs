# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header row
        for row in rows:
            if len(row) < 3:
                print("Skipping invalid row:", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Skipping invalid row:", row)

    return total_cost

import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '/home/labex/project/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)