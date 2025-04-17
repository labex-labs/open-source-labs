#!/bin/zsh

cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Create a stock.py module and a portfolio.csv file for the lab
cat > /home/labex/project/stock.py << 'EOF'
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        self.shares -= amount

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        next(f)  # Skip header
        for line in f:
            fields = line.strip().split(',')
            stock = Stock(fields[0], int(fields[1]), float(fields[2]))
            portfolio.append(stock)
    return portfolio
EOF

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
