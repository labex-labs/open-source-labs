import csv

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys name, shares, and price.
    """

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
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
     
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

def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        stock_name = stock['name']
        shares = stock['shares']
        price = prices.get(stock_name)
        if price is not None:
            change = price - stock['price']
            row = (stock_name, shares, price, change)
            report.append(row)

    return report

portfolio = read_portfolio('/home/labex/project/portfolio.csv')
prices = read_prices('/home/labex/project/prices.csv')
report = make_report(portfolio, prices)
for r in report:
        print(r)


