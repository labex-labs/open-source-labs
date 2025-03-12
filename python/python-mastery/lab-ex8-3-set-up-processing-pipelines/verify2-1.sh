#!/bin/bash
if [ -f /home/labex/project/coticker.py ]; then
  grep -q "to_csv" /home/labex/project/coticker.py \
    && grep -q "create_ticker" /home/labex/project/coticker.py \
    && grep -q "negchange" /home/labex/project/coticker.py \
    && grep -q "ticker" /home/labex/project/coticker.py
  if [ $? -eq 0 ]; then
    echo "Success: coticker.py file contains all required coroutines"
    exit 0
  else
    echo "Error: coticker.py file is missing some required coroutines"
    exit 1
  fi
else
  echo "Error: coticker.py file not found"
  exit 1
fi
