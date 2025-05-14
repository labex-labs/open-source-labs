#!/bin/zsh

# Download initial files for the lab
mkdir -p /home/labex/project
cd /home/labex/project

# Create the initial tableformat.py file
cat > tableformat.py << 'EOF'
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """
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
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """
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
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')

def print_table(records, fields, formatter):
    """
    Print a table of data using the specified formatter.
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [str(getattr(r, fieldname)) for fieldname in fields]
        formatter.row(rowdata)

# Create a simple Stock class for examples
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

# Create a sample portfolio
portfolio = [
    Stock('AA', 100, 32.20),
    Stock('IBM', 50, 91.10),
    Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23),
    Stock('GE', 95, 40.37),
    Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]
EOF

# Set up Python shell history
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
