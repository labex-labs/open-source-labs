#!/bin/bash

cd /home/labex/project

if [ -f "structure.py" ] && [ -f "validate.py" ] && [ -f "reader.py" ] && [ -f "tableformat.py" ] && [ -f "stock.py" ] && [ -f "portfolio.csv" ]; then
  echo "All required files found."
  exit 0
else
  echo "Not all required files exist in the project directory."
  exit 1
fi
