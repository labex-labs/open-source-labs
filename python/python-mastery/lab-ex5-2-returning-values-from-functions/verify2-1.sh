#!/bin/bash
if grep -q "return None" /home/labex/project/return_values.py && grep -q "if len(parts)" /home/labex/project/return_values.py; then
  exit 0
else
  exit 1
fi
