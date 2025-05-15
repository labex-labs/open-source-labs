#!/bin/bash

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash

# Create necessary portfolio data files for the lab
cd /home/labex/project

# Create portfolio.dat file with stock data
cat > portfolio.dat << 'EOF'
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
EOF

# Create portfolio2.dat file with fewer entries
cat > portfolio2.dat << 'EOF'
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
GE 95 40.37
MSFT 50 65.10
EOF

# Create portfolio3.dat with some bad data
cat > portfolio3.dat << 'EOF'
AA 100 32.20
IBM 50 91.10
C - 53.08
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
DIS - 34.20
MSFT 50 65.10
IBM 100 70.44
EOF
