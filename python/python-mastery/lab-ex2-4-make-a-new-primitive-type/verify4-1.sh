#!/bin/bash
if grep -q "@total_ordering" /home/labex/project/mutint.py && grep -q "__eq__" /home/labex/project/mutint.py && grep -q "__lt__" /home/labex/project/mutint.py; then
  echo "Success: Comparison methods and total_ordering decorator were found!"
  exit 0
else
  echo "Error: Comparison methods or total_ordering decorator are missing in mutint.py"
  exit 1
fi
