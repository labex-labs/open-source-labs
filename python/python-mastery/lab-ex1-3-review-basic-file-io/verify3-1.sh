#!/bin/zsh

if grep -q "total_cost += shares \* price" ~/project/pcost.py; then
  echo "Cost calculation code found"
else
  exit 1
fi
