#!/bin/bash

# Check if both formatter classes exist
if grep -q "class CSVTableFormatter" /home/labex/project/tableformat.py \
  && grep -q "class HTMLTableFormatter" /home/labex/project/tableformat.py; then
  # Check if they have the required methods
  if grep -q "def headings" /home/labex/project/tableformat.py \
    && grep -q "def row" /home/labex/project/tableformat.py; then
    exit 0
  else
    echo "One or more formatters are missing required methods."
    exit 1
  fi
else
  echo "One or more formatter classes not found."
  exit 1
fi
