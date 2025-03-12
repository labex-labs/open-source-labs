#!/bin/zsh

# Create stock.py file
cat > /home/labex/project/stock.py << 'EOF'
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
EOF

# Create pcost.py file
cat > /home/labex/project/pcost.py << 'EOF'
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0
    
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    
    return total_cost

# Calculate the cost of portfolio.dat
total = portfolio_cost('portfolio.dat')
print(total)
EOF

# Create portfolio.dat file
cat > /home/labex/project/portfolio.dat << 'EOF'
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
EOF

# Create portfolio2.dat file for testing
cat > /home/labex/project/portfolio2.dat << 'EOF'
AA 75 38.50
IBM 75 91.10
CAT 50 78.44
MSFT 100 65.10
EOF

# Set up Python shell history for easier verification
wget -q https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
