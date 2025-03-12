#!/bin/zsh

# Download and set up the Python shell history script
cd /home/labex/project
wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh
chmod +x .setup-python-shell-history.sh
zsh .setup-python-shell-history.sh

# Make sure we have necessary base files
if [ ! -f "follow.py" ]; then
  cat > follow.py << 'EOF'
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file
    similar to the Unix 'tail -f' command.
    """
    # Open the file and move to the end
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)    # Sleep briefly
            continue
        yield line
EOF
fi

if [ ! -f "structure.py" ]; then
  cat > structure.py << 'EOF'
class Structure:
    _fields = ()
    
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            
    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        return f'{type(self).__name__}' + str(tuple(values)).replace("'", '')
    
    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

class Field:
    def __init__(self):
        self.name = None
        self.type = None
        
    def __set_name__(self, owner, name):
        self.name = name
        owner._fields = owner._fields + (name,)
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class String(Field):
    def __init__(self):
        super().__init__()
        self.type = str
        
class Integer(Field):
    def __init__(self):
        super().__init__()
        self.type = int
        
class Float(Field):
    def __init__(self):
        super().__init__()
        self.type = float
EOF
fi

if [ ! -f "tableformat.py" ]; then
  cat > tableformat.py << 'EOF'
def create_formatter(fmt):
    if fmt == 'text':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError
    
    def row(self, rowdata):
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    def __init__(self):
        self.column_width = 10
        
    def headings(self, headers):
        for h in headers:
            print(f'{h:>{self.column_width}}', end=' ')
        print()
        print('-' * self.column_width * len(headers))
        
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>{self.column_width}}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
        
    def row(self, rowdata):
        formatted = [str(d) for d in rowdata]
        print(','.join(formatted))

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
EOF
fi

if [ ! -f "stocksim.py" ]; then
  cat > stocksim.py << 'EOF'
#!/usr/bin/env python3
# stocksim.py

import time
import csv
import random

def write_quotes():
    """Write randomly generated stock quotes to a CSV file."""
    stocks = {
        'IBM': (103.0, 0.5),
        'AAPL': (124.0, 0.75),
        'MSFT': (30.0, 0.25),
        'HPQ': (35.0, 0.35),
        'YHOO': (29.0, 0.2),
        'CSCO': (27.0, 0.15),
        'AXP': (63.0, 0.4),
        'BA': (98.0, 0.3),
        'C': (53.0, 0.4),
        'CAT': (73.0, 0.35),
        'CVX': (76.0, 0.3),
        'DD': (48.0, 0.25),
        'DIS': (35.0, 0.2),
        'GE': (37.0, 0.15),
        'HD': (38.0, 0.2),
        'HON': (38.0, 0.22),
        'HPQ': (35.0, 0.28),
        'INTC': (25.0, 0.15),
        'JNJ': (62.0, 0.25),
        'JPM': (47.0, 0.32),
        'KO': (52.0, 0.25),
        'MCD': (51.0, 0.3),
        'MMM': (86.0, 0.4),
        'MRK': (44.0, 0.2),
        'PFE': (28.0, 0.15),
        'PG': (63.0, 0.2),
        'T': (40.0, 0.3),
        'UTX': (70.0, 0.4),
        'VZ': (43.0, 0.25),
        'WMT': (50.0, 0.3),
        'XOM': (82.0, 0.35),
        'AA': (40.0, 0.5),
        'AIG': (71.0, 0.45),
    }
    
    with open('stocklog.csv', 'w') as f:
        writer = csv.writer(f)
        for _ in range(10):  # Generate some initial data
            for stock, (price, change) in stocks.items():
                timestamp = time.strftime('%m/%d/%Y %H:%M.%S')
                date, timestr = timestamp.split()
                
                # Generate random price change
                change_amount = random.uniform(-change, change)
                new_price = price + change_amount
                
                # Update the price for next time
                stocks[stock] = (new_price, change)
                
                # Random volume
                volume = int(random.uniform(100000, 1000000))
                
                # Record the quote
                row = [
                    stock,           # Symbol
                    f'{new_price:.2f}',    # Price
                    date,            # Date
                    timestr,         # Time
                    f'{change_amount:.2f}', # Change
                    f'{price:.2f}',         # Open
                    f'{max(price, new_price):.2f}',  # High
                    f'{min(price, new_price):.2f}',  # Low
                    str(volume),     # Volume
                ]
                writer.writerow(row)
                f.flush()
            
            time.sleep(1)

# Run the stock simulation
if __name__ == '__main__':
    write_quotes()
EOF
  chmod +x stocksim.py
  python3 stocksim.py & # Start the simulation in the background
fi

# Create the stocklog.csv file if it doesn't exist
if [ ! -f "stocklog.csv" ]; then
  touch stocklog.csv
  # Start stocksim.py in the background if not already running
  if ! pgrep -f "python3 stocksim.py" > /dev/null; then
    python3 stocksim.py &
  fi
fi
