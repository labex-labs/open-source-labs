#!/bin/bash
cd /home/labex/project

# Check if the subgen and main_gen functions are defined
if grep -q "def subgen" cofollow.py && grep -q "def main_gen" cofollow.py; then
  # Check if yield from is used
  if grep -q "yield from" cofollow.py; then
    echo "Success: Found generator functions with yield from statement"
    exit 0
  else
    echo "Error: Could not find yield from statement in cofollow.py"
    exit 1
  fi
else
  echo "Error: Could not find required generator functions in cofollow.py"
  exit 1
fi
