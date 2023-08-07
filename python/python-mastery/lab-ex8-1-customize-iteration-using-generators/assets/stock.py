# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat


class Stock(Structure):
    name = String("name")
    shares = PositiveInteger("shares")
    price = PositiveFloat("price")

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
