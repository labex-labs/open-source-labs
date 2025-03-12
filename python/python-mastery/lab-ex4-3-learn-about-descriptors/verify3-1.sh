#!/bin/bash
if [ -f "/home/labex/project/validate.py" ]; then
  exit 0
else
  echo "validate.py file not found"
  exit 1
fi
