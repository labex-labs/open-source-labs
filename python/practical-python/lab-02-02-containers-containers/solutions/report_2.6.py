import csv


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


# Test the read_prices() function
prices = read_prices("/home/labex/project/prices.csv")
print(prices)
print(prices["IBM"])
print(prices["MSFT"])
