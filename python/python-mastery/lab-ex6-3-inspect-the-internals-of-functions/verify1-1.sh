#!/bin/bash

# Check if the user has used the basic function inspection commands
if grep -q "def add" /home/labex/.python_history \
  && grep -q "dir(add)" /home/labex/.python_history \
  && grep -q "__name__" /home/labex/.python_history \
  && grep -q "__code__" /home/labex/.python_history; then
  exit 0
else
  exit 1
fi
