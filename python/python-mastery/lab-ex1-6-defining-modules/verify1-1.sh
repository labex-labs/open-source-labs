#!/bin/bash

# Check if the two Python files exist
if [ ! -f /home/labex/project/stock.py ] || [ ! -f /home/labex/project/pcost.py ]; then
  echo "Error: Required Python files are missing."
  exit 1
fi

# Check command history for import statements
history_file="/home/labex/.python_history"
if [ -f "$history_file" ]; then
  if grep -q "import pcost" "$history_file" && grep -q "from stock import Stock" "$history_file"; then
    exit 0
  else
    echo "Error: Could not find evidence of required import statements in your Python history."
    exit 1
  fi
else
  echo "Error: Python history file not found."
  exit 1
fi
