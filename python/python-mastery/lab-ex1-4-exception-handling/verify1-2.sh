#!/bin/bash
output=$(python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio.dat'))")
if [[ $output == *"44671.15"* ]]; then
  exit 0
else
  echo "Portfolio cost calculation incorrect"
  exit 1
fi
