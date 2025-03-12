#!/bin/bash
if grep -q "__add__" /home/labex/project/mutint.py && grep -q "__radd__" /home/labex/project/mutint.py && grep -q "__iadd__" /home/labex/project/mutint.py && grep -q "isinstance" /home/labex/project/mutint.py && grep -q "NotImplemented" /home/labex/project/mutint.py; then
  echo "Success: Math operation methods were found!"
  exit 0
else
  echo "Error: One or more math operation methods are missing in mutint.py"
  exit 1
fi
