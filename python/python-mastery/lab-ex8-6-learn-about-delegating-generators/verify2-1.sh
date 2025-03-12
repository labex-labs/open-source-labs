#!/bin/bash
cd /home/labex/project

# Check if the receive function is defined
if grep -q "def receive" cofollow.py; then
  # Check if the receive function contains the expected code
  if grep -q "msg = yield" cofollow.py && grep -q "isinstance" cofollow.py; then
    echo "Success: Found receive function with proper implementation"
    exit 0
  else
    echo "Error: The receive function doesn't contain the expected code"
    exit 1
  fi
else
  echo "Error: Could not find receive function in cofollow.py"
  exit 1
fi
