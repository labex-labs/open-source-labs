#!/bin/bash
if [[ -f "/home/labex/project/structure.py" && -f "/home/labex/project/stock.py" ]]; then
  echo "Success: Required files found"
  exit 0
else
  echo "Error: Required files not found"
  exit 1
fi
