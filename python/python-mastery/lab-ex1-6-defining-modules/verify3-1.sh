#!/bin/bash

# Check if report.py exists and contains the required functions
if [ -f /home/labex/project/report.py ]; then
  if grep -q "read_portfolio" /home/labex/project/report.py && grep -q "print_report" /home/labex/project/report.py; then
    exit 0
  else
    echo "Error: report.py exists but doesn't contain the required functions."
    exit 1
  fi
else
  echo "Error: report.py does not exist."
  exit 1
fi
