#!/bin/bash
if grep -q "try:" /home/labex/project/pcost.py && grep -q "except ValueError" /home/labex/project/pcost.py; then
  exit 0
else
  echo "Exception handling not properly implemented"
  exit 1
fi
