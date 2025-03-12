#!/bin/bash
if [ -f "/home/labex/project/tableformat.py" ]; then
  exit 0
else
  echo "tableformat.py file not found in the project directory"
  exit 1
fi
