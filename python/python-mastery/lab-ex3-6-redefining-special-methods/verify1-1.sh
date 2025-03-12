#!/bin/bash
grep -q "__repr__" /home/labex/project/stock.py && grep -q "return f\"Stock" /home/labex/project/stock.py
if [ $? -eq 0 ]; then
  echo "Success! You've correctly implemented the __repr__ method."
  exit 0
else
  echo "The __repr__ method was not found or is incorrectly implemented in stock.py."
  exit 1
fi
