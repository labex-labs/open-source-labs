#!/bin/bash
output=$(~/project/function_vars.sh)
if echo "$output" | grep -q "Number of Arguments: 4"; then
  exit 0
else
  exit 1
fi
