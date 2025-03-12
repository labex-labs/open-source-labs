#!/bin/bash
if [ -f /home/labex/project/pcost.py ]; then
  exit 0
else
  echo "pcost.py file not found in the project directory"
  exit 1
fi
