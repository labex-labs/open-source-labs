#!/bin/bash

# Check if map is used in convert_csv
if grep -q "map" /home/labex/project/reader.py \
  && grep -q "convert_csv.*map" /home/labex/project/reader.py; then
  exit 0
else
  exit 1
fi
