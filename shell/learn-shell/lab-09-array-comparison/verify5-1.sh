#!/bin/bash
output=$(~/project/array-comparison.sh)
if echo "$output" | grep -q "5"; then
  exit 0
else
  exit 1
fi
