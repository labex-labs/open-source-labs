#!/bin/bash
if grep -q "__str__" /home/labex/project/mutint.py && grep -q "__repr__" /home/labex/project/mutint.py && grep -q "__format__" /home/labex/project/mutint.py; then
  echo "Success: String representation methods were found!"
  exit 0
else
  echo "Error: One or more string representation methods are missing in mutint.py"
  exit 1
fi
