#!/bin/bash

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
cd ~/project && unzip ctabus.csv.zip && rm ctabus.csv.zip

# Create portfolio.csv
cat > ~/project/portfolio.csv << 'EOF'
name,shares,price
AA,100,32.20
IBM,50,91.10
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.10
HPE,75,32.20
NVDA,100,131.78
EOF

# Create initial stock.py
cat > ~/project/stock.py << 'EOF'
# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with
    keys name, shares, price.
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
EOF

# Create initial reader.py
cat > ~/project/reader.py << 'EOF'
# reader.py
import csv

def read_csv(filename):
    '''
    Read a CSV file into a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            records.append(record)
    return records
EOF
