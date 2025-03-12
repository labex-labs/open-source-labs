#!/bin/bash
cd /home/labex/project
if grep -q "from_row" structure.py \
  && grep -q "zip" structure.py \
  && grep -q "_types" structure.py; then
  exit 0
else
  exit 1
fi
