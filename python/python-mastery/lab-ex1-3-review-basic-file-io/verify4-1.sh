#!/bin/bash
cd ~/project
output=$(python3 ~/project/pcost.py)
if echo "$output" | grep -q "44671"; then
  exit 0
else
  exit 1
fi
