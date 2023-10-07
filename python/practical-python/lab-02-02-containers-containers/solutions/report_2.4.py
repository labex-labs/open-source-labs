import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)  # Skip header row
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

    return portfolio


portfolio = read_portfolio("/home/labex/project/portfolio.csv")

print(portfolio)
print(portfolio[0])
print(portfolio[1])
print(portfolio[1][1])

total = 0.0
for name, shares, price in portfolio:
    total += shares * price

print(total)
