#!/bin/bash
if grep -q "__int__" /home/labex/project/mutint.py && grep -q "__float__" /home/labex/project/mutint.py && grep -q "__index__" /home/labex/project/mutint.py; then
  echo "Success: Type conversion methods were found!"
  exit 0
else
  echo "Error: One or more type conversion methods are missing in mutint.py"
  exit 1
fi
