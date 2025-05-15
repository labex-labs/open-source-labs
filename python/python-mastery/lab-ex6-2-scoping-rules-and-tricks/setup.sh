#!/bin/bash

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash

# Create initial structure.py file
cat > /home/labex/project/structure.py << 'EOF'
class Structure:
    _fields = ()
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)
    
    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'
EOF

# Create initial stock.py file
cat > /home/labex/project/stock.py << 'EOF'
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
EOF

# Create test file
cat > /home/labex/project/teststock.py << 'EOF'
import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    
    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)
    
    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(10)
        self.assertEqual(s.shares, 90)
    
    def test_keyword_args(self):
        s = Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
EOF
