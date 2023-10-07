import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.DictReader(f)
        for row in rows:
            stock = {
                "name": row["name"],
                "shares": int(row["shares"]),
                "price": float(row["price"]),
            }
            portfolio.append(stock)

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
prices = read_prices("/home/labex/project/prices.csv")
report = make_report(portfolio, prices)

headers = ("Name", "Shares", "Price", "Change")


print("%10s %10s %10s %10s" % headers)
print(("-" * 10 + " ") * len(headers))
for row in report:
    print("%10s %10d %10.2f %10.2f" % row)
