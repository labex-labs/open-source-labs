from validate import String, PositiveInteger, PositiveFloat


class Stock:
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
