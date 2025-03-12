#!/bin/bash
if grep -q "def parse_line" /home/labex/project/return_values.py && grep -q "return.*name.*value" /home/labex/project/return_values.py; then
  exit 0
else
  exit 1
fi
