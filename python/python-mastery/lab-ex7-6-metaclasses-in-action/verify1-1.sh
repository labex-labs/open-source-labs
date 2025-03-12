#!/bin/bash
# Check if the files have been accessed
if [ -e /home/labex/project/structure.py ] && [ -e /home/labex/project/validate.py ]; then
  exit 0
else
  exit 1
fi
