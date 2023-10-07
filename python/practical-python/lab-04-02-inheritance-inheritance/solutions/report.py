import sys
import csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
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


def make_report_data(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows = []
    for s in portfolio:
        current_price = prices[s["name"]]
        change = current_price - s["price"]
        summary = (s["name"], s["shares"], current_price, change)
        rows.append(summary)
    return rows


def print_report_txt(report):
    """
    Print the report in text format.
    """
    print("{:<10s} {:<10s} {:<10s} {:<10s}".format("Name", "Shares", "Price", "Change"))
    print("-" * 40)
    for item in report:
        print(
            "{:<10s} {:<10d} {:<10.2f} {:<10.2f}".format(
                item[0], item[1], item[2], item[3]
            )
        )


def print_report_csv(report):
    """
    Print the report in CSV format.
    """
    print(
        "{},{},{},{}".format("Name", "Shares", "Price", "Change")
    )  # Add column headings
    for item in report:
        print("{},{},{},{}".format(item[0], item[1], item[2], item[3]))


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    if fmt == "txt":
        print_report_txt(report)
    elif fmt == "csv":
        print_report_csv(report)
    else:
        print("Unsupported format:", fmt)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 report.py portfoliofile pricefile format")
        sys.exit(1)

    portfoliofile = sys.argv[1]
    pricefile = sys.argv[2]
    output_format = sys.argv[3]

    portfolio_report(portfoliofile, pricefile, output_format)
