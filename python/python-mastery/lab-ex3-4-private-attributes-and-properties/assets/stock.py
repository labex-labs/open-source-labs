# stock.py


class Stock:
    # Do step 4 here

    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    # ------------------------------------------------------------------------------------------ #

    # Do step 3 here

    # TODO: modify the "shares" and "price" attribute as required

    # ------------------------------------------------------------------------------------------ #

    # Do step 2 here

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
