# stock.py


class Stock:
    """
    An instance of a stock holding consisting of name, shares, and price.
    """

    def __init__(self, name, shares, price):
        self._shares = None  # Private attribute to store the value of shares
        self.name = name
        self.shares = shares  # Set the initial value using the property function
        self.price = price

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"


    @property
    def shares(self):
        """
        Get the value of shares
        """
        return self._shares

    @shares.setter
    def shares(self, value):
        """
        Set the value of shares, ensuring it is an integer
        """
        if not isinstance(value, int):
            raise TypeError("Expected an integer")
        self._shares = value

    def cost(self):
        """
        Return the cost of the stock holding (shares * price)
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
