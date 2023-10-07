# pcost_1.31.py

import sys


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        lines = f.readlines()
        headers = lines[0].strip().split(",")
        for line in lines[1:]:
            fields = line.strip().split(",")
            if len(fields) < 3:
                print("Skipping invalid row:", line)
                continue
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Skipping invalid row:", line)

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
