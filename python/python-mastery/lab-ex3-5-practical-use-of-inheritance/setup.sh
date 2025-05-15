#!/bin/bash

# Set up the environment for the lab
mkdir -p /home/labex/project
cd /home/labex/project

# Create the portfolio.csv file
cat > portfolio.csv << 'EOF'
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
EOF

# Create the stock.py file
cat > stock.py << 'EOF'
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
EOF

# Create the reader.py file
cat > reader.py << 'EOF'
import csv

def read_csv_as_instances(filename, classname):
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip headers
        for row in rows:
            if row:  # Skip empty rows
                record = classname(row[0], int(row[1]), float(row[2]))
                records.append(record)
    return records
EOF

# Create initial tableformat.py file
cat > tableformat.py << 'EOF'
def print_table(records, fields):
    """
    Print a table of data from a list of objects.
    """
    # Print field names
    print(' '.join('%10s' % fieldname for fieldname in fields))
    print(('-'*10 + ' ')*len(fields))

    # Print the data
    for record in records:
        rowdata = [getattr(record, fieldname) for fieldname in fields]
        print(' '.join('%10s' % str(d) for d in rowdata))
EOF

# Set up Python shell history
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
