#!/bin/bash
if [ -f /home/labex/project/cofollow.py ]; then
  grep -q "follow" /home/labex/project/cofollow.py && grep -q "consumer" /home/labex/project/cofollow.py && grep -q "printer" /home/labex/project/cofollow.py
  if [ $? -eq 0 ]; then
    echo "Success: cofollow.py file contains the required functions"
    exit 0
  else
    echo "Error: cofollow.py file does not contain all required functions"
    exit 1
  fi
else
  echo "Error: cofollow.py file not found"
  exit 1
fi
