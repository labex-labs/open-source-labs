#!/bin/bash
if ! grep -q "class Stock(myobject)" /home/labex/project/mymeta.py; then
  echo "Stock class not found in mymeta.py"
  exit 1
fi

if ! grep -q "def cost" /home/labex/project/mymeta.py; then
  echo "cost method not found in Stock class"
  exit 1
fi

if ! grep -q "def sell" /home/labex/project/mymeta.py; then
  echo "sell method not found in Stock class"
  exit 1
fi

exit 0
