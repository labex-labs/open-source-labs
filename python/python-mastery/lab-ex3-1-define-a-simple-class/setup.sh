#!/bin/zsh

# Create the initial stock.py file with the Stock class definition
cat > /home/labex/project/stock.py << 'EOF'
# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

# TODO: Add sell(nshares) method here

# TODO: Add read_portfolio(filename) function here

# TODO: Add print_portfolio(portfolio) function here
EOF

# Create the portfolio.csv file for testing
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

wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
