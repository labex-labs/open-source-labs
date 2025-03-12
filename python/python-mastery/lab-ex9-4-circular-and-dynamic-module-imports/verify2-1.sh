#!/bin/bash
if grep -A 2 "def row" ~/project/structly/tableformat/formatter.py | grep -q "from \.formats"; then
  echo "Imports are correctly positioned after the TableFormatter class"
  exit 0
else
  echo "Please ensure the imports are placed after the TableFormatter class definition"
  exit 1
fi
