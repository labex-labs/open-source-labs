#!/bin/bash
output=$(python3 /home/labex/project/pcost.py 2>&1)
if [[ $output == *"Couldn't parse"* ]] && [[ $output == *"44671.15"* ]]; then
  exit 0
else
  echo "Your program doesn't handle bad data correctly"
  exit 1
fi
