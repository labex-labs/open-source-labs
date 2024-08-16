#!/bin/bash
output=$(/home/labex/project/arguments.sh one two three four)
if echo "$output" | grep -q "4"; then
  exit 0
else
  exit 1
fi
