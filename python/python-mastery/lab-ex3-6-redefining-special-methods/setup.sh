#!/bin/zsh

# Download and set up Python shell history
cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Create the stock.py file with the initial Stock class implementation
cat > /home/labex/project/stock.py << 'EOF'
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        return self.shares * self.price
        
    def sell(self, shares):
        self.shares -= shares
EOF

# Create a sample portfolio.csv file
cat > /home/labex/project/portfolio.csv << 'EOF'
name,shares,price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.10
IBM,100,70.44
EOF

# Create reader.py with read_csv_as_instances function
cat > /home/labex/project/reader.py << 'EOF'
import csv

def read_csv_as_instances(filename, cls):
    """
    Read a CSV file and create a list of instances of a given class
    """
    instances = []
    with open(filename) as f:
        reader = csv.reader(f)
        headers = next(reader)  # Skip header row
        for row in reader:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            instances.append(cls(name, shares, price))
    return instances
EOF

# Create tableformat.py file
cat > /home/labex/project/tableformat.py << 'EOF'
import sys

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
        
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))
        
    def row(self, rowdata):
        for item in rowdata:
            print(f'{item:>10s}', end=' ')
        print()

def create_formatter(format_name):
    if format_name == 'text':
        return TextTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
        
def print_table(data, columns, formatter):
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
EOF
