#!/bin/bash

# Check if TableFormatter class exists with required methods
if grep -q "class TableFormatter" /home/labex/project/tableformat.py \
  && grep -q "def headings" /home/labex/project/tableformat.py \
  && grep -q "def row" /home/labex/project/tableformat.py \
  && grep -q "raise NotImplementedError" /home/labex/project/tableformat.py; then
  # Check if print_table function has been updated
  if grep -q "def print_table.*formatter" /home/labex/project/tableformat.py \
    && grep -q "formatter.headings" /home/labex/project/tableformat.py \
    && grep -q "formatter.row" /home/labex/project/tableformat.py; then
    exit 0
  else
    echo "print_table function has not been properly updated."
    exit 1
  fi
else
  echo "TableFormatter class not found or missing required methods."
  exit 1
fi
