#!/bin/bash

if [ ! -f /home/labex/project/reader.py ]; then
  echo "Error: reader.py file not found"
  exit 1
fi

# Check for header parameter and handling
grep -q "headers=None" /home/labex/project/reader.py
grep -q "if headers is None" /home/labex/project/reader.py

# Check functionality in both functions
grep -q "def csv_as_dicts.*headers=None" /home/labex/project/reader.py
grep -q "def csv_as_instances.*headers=None" /home/labex/project/reader.py
grep -q "def read_csv_as_dicts.*headers=None" /home/labex/project/reader.py
grep -q "def read_csv_as_instances.*headers=None" /home/labex/project/reader.py

if [ $? -eq 0 ]; then
  echo "reader.py correctly handles optional headers"
  exit 0
else
  echo "reader.py is missing some header handling functionality"
  exit 1
fi
