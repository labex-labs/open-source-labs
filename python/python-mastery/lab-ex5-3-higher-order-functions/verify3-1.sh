#!/bin/bash

# Check if both functions use convert_csv
if grep -q "convert_csv" /home/labex/project/reader.py \
  && grep -q "csv_as_dicts.*convert_csv" /home/labex/project/reader.py \
  && grep -q "csv_as_instances.*convert_csv" /home/labex/project/reader.py; then
  exit 0
else
  exit 1
fi
