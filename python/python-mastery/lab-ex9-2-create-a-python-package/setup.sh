#!/bin/zsh

# Download and set up necessary files
mkdir -p /home/labex/project
cd /home/labex/project

# Create the structure.py file
cat > structure.py << 'EOF'
from validate import validate_type, PositiveInteger, PositiveFloat, String

class Structure:
    _fields = None
    
    def __init__(self, *args, **kwargs):
        if self._fields is None:
            self._fields = {}
            for cls in self.__class__.__mro__:
                for key, value in cls.__dict__.items():
                    if isinstance(value, Descriptor):
                        self._fields[key] = value
        
        # Process positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)
            
        # Process keyword arguments
        for name, val in kwargs.items():
            setattr(self, name, val)
    
    def __repr__(self):
        attrs = [f'{key}={getattr(self, key)!r}' for key in self._fields]
        return f'{self.__class__.__name__}({", ".join(attrs)})'
    
    @classmethod
    def from_row(cls, row):
        rowdata = { key: func(val) for key, func, val in 
                   zip(cls._fields, [x.converter for x in cls._fields.values()], row) }
        return cls(**rowdata)

class Descriptor:
    def __init__(self, name=None):
        self.name = name
        
    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.converter(value)
        
    def __set_name__(self, owner, name):
        self.name = name

class Typed(Descriptor):
    ty = object
    converter = lambda self, x: x
    
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            value = self.converter(value)
        super().__set__(instance, value)

class Integer(Typed):
    ty = int
    converter = int
        
class Float(Typed):
    ty = float
    converter = float
    
class String(Typed):
    ty = str
    converter = str
    
class PositiveInteger(Integer):
    def __set__(self, instance, value):
        value = validate_type(value, self.name, self.ty, self.converter)
        if value <= 0:
            raise ValueError(f'{self.name} must be > 0')
        instance.__dict__[self.name] = value
    
class PositiveFloat(Float):
    def __set__(self, instance, value):
        value = validate_type(value, self.name, self.ty, self.converter)
        if value <= 0:
            raise ValueError(f'{self.name} must be > 0')
        instance.__dict__[self.name] = value
EOF

# Create the validate.py file
cat > validate.py << 'EOF'
def validate_type(value, name, expected_type, converter):
    if not isinstance(value, expected_type):
        try:
            return converter(value)
        except (TypeError, ValueError):
            raise TypeError(f'{name} must be of type {expected_type.__name__}')
    return value
EOF

# Create the reader.py file
cat > reader.py << 'EOF'
import csv

def read_csv_as_dicts(filename, types=None):
    '''
    Read a CSV file into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            if types:
                for key, type_func in types.items():
                    if key in record:
                        record[key] = type_func(record[key])
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
EOF

# Create the tableformat.py file
cat > tableformat.py << 'EOF'
class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        for item in rowdata:
            print(f'{item:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        for item in rowdata:
            print(f'<td>{item}</td>', end='')
        print('</tr>')

def create_formatter(fmt):
    if fmt == 'text':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for record in records:
        row_data = [getattr(record, field) for field in fields]
        formatter.row(row_data)
EOF

# Create the stock.py file
cat > stock.py << 'EOF'
# stock.py

from structure import Structure, String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from reader import read_csv_as_instances
    from tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
EOF

# Create the portfolio.csv file
cat > portfolio.csv << 'EOF'
name,shares,price
MSFT,100,51.23
IBM,50,91.1
AAPL,75,145.89
ACME,125,123.45
HPE,75,32.2
EOF

wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
