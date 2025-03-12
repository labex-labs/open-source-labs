#!/bin/bash

# Check if the convert_csv function exists in reader.py
if grep -q "def convert_csv" /home/labex/project/reader.py; then
  exit 0
else
  exit 1
fi
