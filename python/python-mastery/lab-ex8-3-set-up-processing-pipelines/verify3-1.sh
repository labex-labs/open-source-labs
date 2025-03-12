#!/bin/bash
if [ -f /home/labex/project/coticker.py ]; then
  grep -q "filter_by_name" /home/labex/project/coticker.py \
    && grep -q "price_threshold" /home/labex/project/coticker.py
  if [ $? -eq 0 ]; then
    echo "Success: Enhanced coticker.py contains the new filtering coroutines"
    exit 0
  else
    echo "Error: coticker.py is missing the new filtering coroutines"
    exit 1
  fi
else
  echo "Error: coticker.py file not found"
  exit 1
fi
