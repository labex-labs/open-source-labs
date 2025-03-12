#!/bin/bash
grep -q "__eq__" /home/labex/project/stock.py && grep -q "isinstance" /home/labex/project/stock.py
if [ $? -eq 0 ]; then
  echo "Success! You've correctly implemented the __eq__ method."
  exit 0
else
  echo "The __eq__ method was not found or is missing the isinstance check in stock.py."
  exit 1
fi
