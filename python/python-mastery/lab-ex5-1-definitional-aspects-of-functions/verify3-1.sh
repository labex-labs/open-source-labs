#!/bin/bash

if [ ! -f /home/labex/project/reader.py ]; then
  echo "Error: reader.py file not found"
  exit 1
fi

# Check for the new functions
grep -q "def csv_as_dicts" /home/labex/project/reader.py
grep -q "def csv_as_instances" /home/labex/project/reader.py

# Check the refactoring of original functions
grep -q "with open(filename) as file:" /home/labex/project/reader.py
grep -q "return csv_as_dicts" /home/labex/project/reader.py
grep -q "return csv_as_instances" /home/labex/project/reader.py

if [ $? -eq 0 ]; then
  echo "reader.py has been properly refactored"
  exit 0
else
  echo "reader.py is missing some of the refactored elements"
  exit 1
fi
