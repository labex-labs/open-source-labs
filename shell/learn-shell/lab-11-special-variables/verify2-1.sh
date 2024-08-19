#!/bin/bash
output=$(~/project/special_vars.sh)
if echo "$output" | grep -q "Number of Arguments: 0"; then
  exit 0
else
  exit 1
fi
