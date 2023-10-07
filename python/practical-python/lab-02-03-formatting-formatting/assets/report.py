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
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Skip empty lines
                    stock_name = row[0]
                    stock_price = float(row[1])
                    prices[stock_name] = stock_price
    except IndexError:
        pass

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