#!/bin/bash

if [ ! -f /home/labex/project/reader.py ]; then
  echo "Error: reader.py file not found"
  exit 1
fi

# Check for importing types from typing module
grep -q "from typing import" /home/labex/project/reader.py

# Check for type hint annotations
grep -q "def csv_as_dicts.*) -> List" /home/labex/project/reader.py
grep -q "def csv_as_instances.*) -> List" /home/labex/project/reader.py
grep -q "Optional\[List\[str\]\]" /home/labex/project/reader.py

# Check for TypeVar usage
grep -q "TypeVar" /home/labex/project/reader.py

if [ $? -eq 0 ]; then
  echo "reader.py correctly includes type hints"
  exit 0
else
  echo "reader.py is missing some type hint elements"
  exit 1
fi
