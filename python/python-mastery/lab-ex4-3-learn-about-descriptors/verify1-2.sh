#!/bin/bash
grep -q "property" /home/labex/project/stock.py \
  && grep -q "__slots__" /home/labex/project/stock.py \
  && grep -q "__init__" /home/labex/project/stock.py
if [ $? -eq 0 ]; then
  exit 0
else
  echo "Stock class does not contain required methods"
  exit 1
fi
