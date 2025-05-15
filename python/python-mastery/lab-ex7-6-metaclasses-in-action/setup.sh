#!/bin/bash
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash

# Set up the necessary files for the lab
cd /home/labex/project

# Create the necessary files
cat > structure.py << 'EOF'
class Structure:
    _fields = []
    
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
            
        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)
            
        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)
            
    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
EOF

cat > validate.py << 'EOF'
from inspect import signature
import re

class Validator:
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value
        
    def validate(self, value):
        pass

class Typed(Validator):
    expected_type = object
    
    def validate(self, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
            
class Positive(Validator):
    def validate(self, value):
        if value <= 0:
            raise ValueError('Expected > 0')
            
class NonEmpty(Validator):
    def validate(self, value):
        if len(value) == 0:
            raise ValueError('Cannot be empty')
            
class String(Typed):
    expected_type = str
    
class Integer(Typed):
    expected_type = int
    
class Float(Typed):
    expected_type = float
    
class PositiveInteger(Integer, Positive):
    pass
    
class PositiveFloat(Float, Positive):
    pass
    
class NonEmptyString(String, NonEmpty):
    pass
EOF

cat > teststock.py << 'EOF'
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
        s.sell(20)
        self.assertEqual(s.shares, 80)
        
    def test_bad_shares(self):
        with self.assertRaises(TypeError):
            s = Stock('GOOG', '100', 490.1)
            
    def test_bad_price(self):
        with self.assertRaises(TypeError):
            s = Stock('GOOG', 100, 'a lot')
            
    def test_bad_sell(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.sell('all')
            
if __name__ == '__main__':
    unittest.main()
EOF

cat > portfolio.csv << 'EOF'
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
EOF

cat > reader.py << 'EOF'
import csv

def read_csv(filename):
    """
    Read a CSV file into a list of dicts
    """
    with open(filename) as f:
        return list(csv.DictReader(f))

def read_csv_as_instances(filename, cls):
    """
    Read a CSV file into a list of instances
    """
    records = read_csv(filename)
    return [cls(**row) for row in records]
EOF

cat > tableformat.py << 'EOF'
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError
        
    def row(self, rowdata):
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join(f'{h:>10}' for h in headers))
        print('-'*10*len(headers))
        
    def row(self, rowdata):
        print(' '.join(f'{d:>10}' for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
        
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
        
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

def create_formatter(name):
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {name}')

def print_table(objects, attrs, formatter):
    formatter.headings(attrs)
    for obj in objects:
        rowdata = [getattr(obj, attr) for attr in attrs]
        formatter.row(rowdata)
EOF
