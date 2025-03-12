#!/bin/bash

# Check if the user has used the inspect module
if grep -q "import inspect" /home/labex/.python_history \
  && grep -q "inspect.signature" /home/labex/.python_history \
  && grep -q "parameters" /home/labex/.python_history \
  && grep -q "tuple" /home/labex/.python_history; then
  exit 0
else
  exit 1
fi
