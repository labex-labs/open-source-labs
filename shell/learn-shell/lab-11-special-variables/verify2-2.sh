#!/bin/bash
output=$(~/project/special_vars.sh hello world)
if echo "$output" | grep -q "First Argument: hello"; then
  exit 0
else
  exit 1
fi
