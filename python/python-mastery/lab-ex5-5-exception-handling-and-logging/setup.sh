#!/bin/zsh

# Create the project directory structure
cd /home/labex/project

# Create the reader.py file with initial code
cat > reader.py << 'EOF'
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []
    return list(map(lambda row: converter(headers, row), rows))

def csv_as_dicts(filename, types, headers=None):
    """
    Read CSV data into a list of dictionaries with column type conversion
    """
    import csv
    with open(filename) as f:
        rows = csv.reader(f)
        return convert_csv(rows, 
            lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })

def read_csv_as_dicts(filename, types, headers=None):
    """
    Read a CSV file into a list of dictionaries with appropriate type conversion
    """
    return csv_as_dicts(filename, types, headers=headers)
EOF

# Create a missing.csv file with some bad data
cat > missing.csv << 'EOF'
name,shares,price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
C,,53.08
MSFT,200,51.23
GE,95,40.37
DIS,50,N/A
GE,,37.23
HPQ,75,32.51
INTC,100,30.00
AAPL,125,99.30
INTC,,21.84
MSFT,200,51.23
HPQ,75,32.51
IBM,50,91.10
MCD,,51.11
MSFT,200,51.23
MO,,70.09
MSFT,200,51.23
PFE,,26.40
MSFT,200,51.23
GE,95,40.37
MSFT,200,51.23
VZ,,42.92
XOM,300,83.00
EOF

# Create a valid.csv file for comparison
cat > valid.csv << 'EOF'
name,shares,price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
HPQ,75,32.51
INTC,100,30.00
AAPL,125,99.30
MSFT,200,51.23
HPQ,75,32.51
IBM,50,91.10
MSFT,200,51.23
MSFT,200,51.23
MSFT,200,51.23
GE,95,40.37
MSFT,200,51.23
XOM,300,83.00
EOF

# Set up shell history for better user experience
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
