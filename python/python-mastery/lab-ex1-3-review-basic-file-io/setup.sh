#!/bin/zsh

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
touch ~/project/pcost.py

# Create the portfolio.dat file
cat > ~/project/portfolio.dat << EOL
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
EOL
