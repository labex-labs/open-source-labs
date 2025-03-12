#!/bin/bash

cd /home/labex/project

if grep -q "from structly.structure import" "stock.py" \
  && grep -q "from structly.reader import" "stock.py" \
  && grep -q "from structly.tableformat import" "stock.py"; then
  echo "stock.py has been updated correctly to import from the structly package."

  # Try running the script to check if it works
  output=$(python stock.py)
  if [ $? -eq 0 ]; then
    echo "stock.py runs successfully with the new package structure."
    exit 0
  else
    echo "stock.py fails to run with the new package structure."
    exit 1
  fi
else
  echo "stock.py has not been updated correctly to import from the structly package."
  exit 1
fi
