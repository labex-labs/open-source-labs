#!/bin/bash

# Check if the necessary files exist
if [ -f /home/labex/project/tableformat.py ] && [ -f /home/labex/project/stock.py ] && [ -f /home/labex/project/reader.py ]; then
  exit 0
else
  echo "Required files not found. Please make sure all necessary files are created."
  exit 1
fi
