#!/bin/zsh

# Setup for the Python attribute access lab
mkdir -p /home/labex/project
cd /home/labex/project

# Create stock.py for our examples
cat > /home/labex/project/stock.py << 'EOF'
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def cost(self):
        return self.shares * self.price
EOF

# Setup Python shell history tracking
cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
