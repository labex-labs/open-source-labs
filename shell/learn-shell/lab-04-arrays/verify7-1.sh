#!/bin/bash
output=$(~/project/arrays.sh)
if echo "$output" | grep -q "NUMBERS array: 1 2 3" \
  && echo "$output" | grep -q "The second name on the NAMES list is: Eric"; then
  exit 0
else
  exit 1
fi
