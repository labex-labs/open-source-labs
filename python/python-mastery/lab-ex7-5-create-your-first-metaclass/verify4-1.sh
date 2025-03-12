#!/bin/bash
if ! grep -q "class MyStock(Stock)" /home/labex/project/mymeta.py; then
  echo "MyStock class not found in mymeta.py"
  exit 1
fi

if ! grep -q "def info" /home/labex/project/mymeta.py; then
  echo "info method not found in MyStock class"
  exit 1
fi

exit 0
