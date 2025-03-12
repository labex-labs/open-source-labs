#!/bin/bash
if grep -q "class MutInt" /home/labex/project/mutint.py && grep -q "__init__" /home/labex/project/mutint.py && grep -q "__slots__" /home/labex/project/mutint.py; then
  echo "Success: MutInt class with __init__ method was found!"
  exit 0
else
  echo "Error: MutInt class with __init__ method not found in mutint.py"
  exit 1
fi
