# Step 3 Solution


# validate.py


class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


# stock.py

from validate import *


class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
