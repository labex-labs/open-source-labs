#!/bin/bash

# Run the Python script and capture the output in the file "debug5"
python3 ~/project/mortgage.py > debug5

# Check if the string "0.00" is present in the file "debug5"
zero_output=$(grep "0" debug5)

# Check if the line "< 0" or "<0" exists in the file ~/project/mortgage.py
negative_check=$(grep -E "<\s*0" ~/project/mortgage.py)

# If the string "0.00" is in the output, and the negative check line exists, print "True"
if [ -n "$zero_output" ] && [ -n "$negative_check" ]; then
  echo "True"
fi
