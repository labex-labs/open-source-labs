#!/bin/bash
if grep -q "@classmethod" ~/project/stock.py && grep -q "from_row" ~/project/stock.py && grep -q "types = " ~/project/stock.py; then
  exit 0
else
  exit 1
fi
