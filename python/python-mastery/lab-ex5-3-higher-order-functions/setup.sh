#!/bin/bash

# Create the initial reader.py file
cat > /home/labex/project/reader.py << 'EOL'
#!/usr/bin/env python3
# reader.py
import csv

def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
EOL

# Create the portfolio.csv file
cat > /home/labex/project/portfolio.csv << 'EOL'
name,shares,price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.10
IBM,100,70.44
EOL

# Download the common scripts for Python shell history
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
