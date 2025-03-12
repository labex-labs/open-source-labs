#!/bin/bash

# Check if the file has been modified to include logging
if grep -q "import logging" /home/labex/project/reader.py && grep -q "logger" /home/labex/project/reader.py; then
  exit 0
else
  echo "The reader.py file should be modified to use the logging module"
  exit 1
fi
