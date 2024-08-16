#!/bin/bash
output=$(./arguments.sh one two three four)
if echo "$output" | grep -q "Total number of arguments: 4"; then
  exit 0
else
  exit 1
fi
