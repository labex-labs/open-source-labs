#!/bin/bash

# Create necessary files for the lab
cd /home/labex/project

# Create stock.py module
cat > stock.py << 'EOF'
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))
EOF

# Create portfolio.csv
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

# Create portfolio_noheader.csv
cat > portfolio_noheader.csv << 'EOF'
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
EOF

# Create compressed version
gzip -c portfolio.csv > portfolio.csv.gz

# Setup shell history
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
