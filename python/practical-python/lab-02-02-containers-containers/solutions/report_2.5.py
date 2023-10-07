import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.DictReader(f)
        for row in rows:
            holding = {
                'name': row['name'],
                'shares': int(row['shares']),
                'price': float(row['price'])
            }
            portfolio.append(holding)

    return portfolio

portfolio = read_portfolio('/home/labex/project/portfolio.csv')

print(portfolio)
print(portfolio[0])
print(portfolio[1])
print(portfolio[1]['shares'])

total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']

print(total)