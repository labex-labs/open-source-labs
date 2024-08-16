#!/bin/bash
output=$(/home/labex/project/arguments.sh apple banana cherry date)
if echo "$output" | grep -q "date"; then
  exit 0
else
  exit 1
fi
