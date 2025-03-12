#!/bin/bash

# Check if pcost.py contains the __main__ check
if grep -q "__name__" /home/labex/project/pcost.py && grep -q "__main__" /home/labex/project/pcost.py; then
  exit 0
else
  echo "Error: Could not find the __name__ == \"__main__\" check in pcost.py"
  exit 1
fi
