#!/bin/bash
if [ -f "/home/labex/project/stock.py" ]; then
  exit 0
else
  echo "stock.py file not found"
  exit 1
fi
