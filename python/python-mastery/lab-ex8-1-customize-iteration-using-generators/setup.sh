#!/bin/zsh

# Set up Python shell history for this lab
cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Create necessary files for the lab
cat > /home/labex/project/structure.py << 'EOF'
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
EOF

cat > /home/labex/project/stock.py << 'EOF'
from structure import Structure

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
EOF

cat > /home/labex/project/teststock.py << 'EOF'
import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_creation(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_equality(self):
        s1 = Stock('GOOG', 100, 490.1)
        s2 = Stock('GOOG', 100, 490.1)
        self.assertEqual(s1, s2)

if __name__ == '__main__':
    unittest.main()
EOF

cat > /home/labex/project/stocksim.py << 'EOF'
import csv
import random
import time

def write_stock_data():
    stocks = [
        ('AAPL', 150.0, 0.0, 0.0, 0.0),
        ('GOOG', 2500.0, 0.0, 0.0, 0.0),
        ('MSFT', 300.0, 0.0, 0.0, 0.0),
        ('AMZN', 3300.0, 0.0, 0.0, 0.0),
        ('TSLA', 700.0, 0.0, 0.0, 0.0)
    ]
    
    with open('stocklog.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(10):
            for i in range(len(stocks)):
                name, price, _, _, _ = stocks[i]
                change = round(random.uniform(-5.0, 5.0), 2)
                new_price = round(price + change, 2)
                percent_change = round((change / price) * 100, 2)
                stocks[i] = (name, new_price, price, percent_change, change)
                writer.writerow([f'"{name}"', new_price, price, percent_change, change])
                f.flush()
                time.sleep(0.5)
    
    print("Stock simulation completed!")

if __name__ == "__main__":
    write_stock_data()
EOF
