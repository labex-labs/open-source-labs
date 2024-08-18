#!/bin/zsh
output=$(~/project/array-comparison.sh)
if echo "$output" | grep -q "Common elements among a, b, and c:"; then
  exit 0
else
  exit 1
fi
