#!/bin/bash
if [ -f "/home/labex/project/descrip.py" ]; then
  exit 0
else
  echo "descrip.py file not found"
  exit 1
fi
