#!/bin/bash

cat > /home/labex/project/stock.py << 'EOF'
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        if value < 0:
            raise ValueError('shares cannot be negative')
        self._shares = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected int or float')
        if value < 0:
            raise ValueError('price cannot be negative')
        self._price = value
    
    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        self.shares -= amount
        return self.shares
    
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))
    
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
    def __eq__(self, other):
        return (self.name == other.name and
                self.shares == other.shares and
                self.price == other.price)
EOF

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
