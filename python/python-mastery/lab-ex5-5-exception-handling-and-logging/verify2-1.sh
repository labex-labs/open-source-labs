#!/bin/bash

# Check if the file has been modified to include try-except
if grep -q "try:" /home/labex/project/reader.py && grep -q "except" /home/labex/project/reader.py; then
  exit 0
else
  echo "The reader.py file should be modified to include try-except blocks for exception handling"
  exit 1
fi
