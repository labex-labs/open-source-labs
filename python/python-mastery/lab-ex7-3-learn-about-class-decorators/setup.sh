#!/bin/zsh

# Download and run the setup script
wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Create the necessary files for the lab
cat > ~/project/validate.py << 'EOF'
class Validator:
    def __init__(self, name=None):
        self.name = name
    
    def __set_name__(self, cls, name):
        if self.name is None:
            self.name = name
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value
    
    def validate(self, value):
        pass

class String(Validator):
    expected_type = str
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'{self.name} must be a string')

class PositiveInteger(Validator):
    expected_type = int
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'{self.name} must be an integer')
        if value < 0:
            raise ValueError(f'{self.name} must be >= 0')

class PositiveFloat(Validator):
    expected_type = float
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'{self.name} must be a float')
        if value < 0:
            raise ValueError(f'{self.name} must be >= 0')

def validated(func):
    import inspect
    sig = inspect.signature(func)
    annotations = func.__annotations__
    
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in annotations:
                annotations[name].validate(val)
        return func(*args, **kwargs)
    
    return wrapper
EOF

cat > ~/project/structure.py << 'EOF'
class Structure:
    _fields = ()
    
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)
    
    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'
    
    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'
        
        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])
EOF

cat > ~/project/teststock.py << 'EOF'
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
        s.sell(25)
        self.assertEqual(s.shares, 75)
    
    def test_validate_string(self):
        with self.assertRaises(TypeError):
            s = Stock(100, 100, 490.1)
    
    def test_validate_integer(self):
        with self.assertRaises(TypeError):
            s = Stock('GOOG', 'hundred', 490.1)
    
    def test_validate_float(self):
        with self.assertRaises(TypeError):
            s = Stock('GOOG', 100, 'four-ninety')
    
    def test_validate_positive_shares(self):
        with self.assertRaises(ValueError):
            s = Stock('GOOG', -100, 490.1)
    
    def test_validate_positive_price(self):
        with self.assertRaises(ValueError):
            s = Stock('GOOG', 100, -490.1)
    
    def test_validate_sell_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.sell('25')

if __name__ == '__main__':
    unittest.main()
EOF

cat > ~/project/portfolio.csv << 'EOF'
name,shares,price
GOOG,100,490.1
AAPL,50,545.75
MSFT,200,30.47
EOF

cat > ~/project/reader.py << 'EOF'
import csv

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
EOF

# Create initial stock.py file
cat > ~/project/stock.py << 'EOF'
# This is a placeholder file
# You'll modify it during the lab
EOF
EOF
