# Exercise 2.7: Finding out if you can retire

Tie all of this work together by adding a few additional statements to your `report.py` program that computes gain/loss. These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.

Here's a solution:

```python
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

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                stock_name = row[0]
                stock_price = float(row[1])
                prices[stock_name] = stock_price

    return prices

portfolio = read_portfolio('/home/labex/project/portfolio.csv')
prices = read_prices('/home/labex/project/prices.csv')

total = 0.0
for stock in portfolio:
    stock_name = stock['name']
    shares = stock['shares']
    price = prices.get(stock_name)
    if price is not None:
        value = shares * price
        stock['value'] = value
        total += value

print("Current value of the portfolio: $", total)

cost = 0.0
for stock in portfolio:
    cost += stock['shares'] * stock['price']

gain_loss = total - cost
print("Gain/Loss: $", gain_loss)
```