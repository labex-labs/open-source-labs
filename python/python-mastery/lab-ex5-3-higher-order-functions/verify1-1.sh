#!/bin/bash

# Check if reader.py exists
if [ -f /home/labex/project/reader.py ]; then
  exit 0
else
  exit 1
fi
