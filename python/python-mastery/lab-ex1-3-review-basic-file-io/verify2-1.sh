#!/bin/zsh

if grep -q "with open" ~/project/pcost.py && grep -q "for line in file" ~/project/pcost.py; then
  echo "File reading code found"
else
  exit 1
fi
