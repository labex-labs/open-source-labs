#!/bin/bash

# Check if create_formatter function exists
if grep -q "def create_formatter" /home/labex/project/tableformat.py; then
  # Check if it handles all three formats
  if grep -q "format_name.*text" /home/labex/project/tableformat.py \
    && grep -q "format_name.*csv" /home/labex/project/tableformat.py \
    && grep -q "format_name.*html" /home/labex/project/tableformat.py; then
    exit 0
  else
    echo "create_formatter function doesn't handle all required formats."
    exit 1
  fi
else
  echo "create_formatter function not found."
  exit 1
fi
