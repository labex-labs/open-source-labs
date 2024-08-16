#!/bin/bash
output=$(./arguments.sh apple banana cherry date)
if echo "$output" | grep -q "Total number of arguments: 4" \
  && echo "$output" | grep -q "Argument 1: apple" \
  && echo "$output" | grep -q "Argument 2: banana" \
  && echo "$output" | grep -q "Argument 3: cherry" \
  && echo "$output" | grep -q "Argument 4: date"; then
  exit 0
else
  exit 1
fi
