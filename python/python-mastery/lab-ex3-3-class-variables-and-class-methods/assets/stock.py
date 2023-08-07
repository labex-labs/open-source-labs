# stock.py


class Stock:
    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def from_row(cls, row):
        pass
        # TODO: implement this function

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename):
    """
    Read a CSV file of stock data into a list of Stocks
    """
    pass
    # TODO: implement this function


if __name__ == "__main__":
    import tableformat
    import reader

    # portfolio = read_portfolio('/home/labex/project/portfolio.csv')
    portfolio = reader.read_csv_as_instances("/home/labex/project/portfolio.csv", Stock)
    tableformat.print_table(portfolio, ["name", "shares", "price"])
