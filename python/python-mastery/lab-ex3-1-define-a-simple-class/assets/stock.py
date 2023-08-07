# stock.py


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price


def read_portfolio(filename):
    """
    Read a CSV file of stock data into a list of Stocks
    """
    pass
    # TODO: implement this function


def print_portfolio(portfolio):
    """
    Make a nicely formatted table showing stock data
    """
    pass
    # TODO: implement this function


if __name__ == "__main__":
    portfolio = read_portfolio("/home/labex/project/portfolio.csv")
    print_portfolio(portfolio)
