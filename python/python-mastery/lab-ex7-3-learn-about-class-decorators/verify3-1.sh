#!/bin/bash
cd /home/labex/project
if grep -q "__init_subclass__" structure.py \
  && ! grep -q "@validate_attributes" stock.py; then
  exit 0
else
  exit 1
fi
