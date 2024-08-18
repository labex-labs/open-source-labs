#!/bin/bash
output=$(bash /home/labex/project/string_logic.sh)
if [[ $output == *"Both strings match"* ]]; then
  exit 0
else
  exit 1
fi
