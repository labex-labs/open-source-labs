#!/bin/zsh

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash

# Download the necessary files for the lab
mkdir -p /home/labex/project
cd /home/labex/project

# Create tableformat.py with initial content
cat > tableformat.py << 'EOF'
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
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

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')

def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
EOF

# Create stock.py with initial content
cat > stock.py << 'EOF'
# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))
EOF

# Create reader.py with initial content
cat > reader.py << 'EOF'
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
EOF

# Create portfolio.csv with sample data
cat > portfolio.csv << 'EOF'
name,shares,price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.10
IBM,100,70.44
EOF
