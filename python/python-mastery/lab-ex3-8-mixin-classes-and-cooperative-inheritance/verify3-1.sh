#!/bin/bash
grep -q "def create_formatter.*column_formats" "/home/labex/project/tableformat.py" && grep -q "upper_headers" "/home/labex/project/tableformat.py"
if [ $? -eq 0 ]; then
  exit 0
else
  echo "The create_formatter function hasn't been properly enhanced"
  exit 1
fi
