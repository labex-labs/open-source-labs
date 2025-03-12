#!/bin/bash
if grep -q "self._init()" /home/labex/project/stock.py; then
  echo "Success: Stock class has been updated to use _init"
  exit 0
else
  echo "Error: stock.py does not call self._init()"
  exit 1
fi
