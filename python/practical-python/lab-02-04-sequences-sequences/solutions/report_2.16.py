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
            holding = {
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    prices = {}
    try:
        with open(filename, "r") as file:
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
        stock_name = stock["name"]
        shares = stock["shares"]
        price = prices.get(stock_name)
        if price is not None:
            change = price - stock["price"]
            row = (stock_name, shares, price, change)
            report.append(row)

    return report


portfolio = read_portfolio("/home/labex/project/portfolio.csv")
print(portfolio)
