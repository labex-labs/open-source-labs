#!/bin/bash

if [ ! -f /home/labex/project/reader.py ]; then
  echo "Error: reader.py file not found"
  exit 1
fi

# Check for key elements in the reader.py file
grep -q "import csv" /home/labex/project/reader.py
grep -q "def read_csv_as_dicts" /home/labex/project/reader.py
grep -q "def read_csv_as_instances" /home/labex/project/reader.py
grep -q "with open(filename) as file" /home/labex/project/reader.py
grep -q "headers = next(rows)" /home/labex/project/reader.py
grep -q "records.append" /home/labex/project/reader.py

if [ $? -eq 0 ]; then
  echo "reader.py contains the required functions and code structure"
  exit 0
else
  echo "reader.py is missing some required elements"
  exit 1
fi
