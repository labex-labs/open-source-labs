#!/bin/bash
output=$(./arguments.sh apple banana cherry date)
if echo "$output" | grep -q "Argument 4: date"; then
  exit 0
else
  exit 1
fi
