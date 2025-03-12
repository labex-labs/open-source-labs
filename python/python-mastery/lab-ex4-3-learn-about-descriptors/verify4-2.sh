#!/bin/bash
if [ -f "/home/labex/project/improved_stock.py" ]; then
  grep -q "name = String()" /home/labex/project/improved_stock.py
  if [ $? -eq 0 ]; then
    exit 0
  else
    echo "The improved Stock class does not use the simplified descriptor syntax"
    exit 1
  fi
else
  echo "improved_stock.py file not found"
  exit 1
fi
