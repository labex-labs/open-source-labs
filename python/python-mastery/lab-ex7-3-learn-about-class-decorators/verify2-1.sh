#!/bin/bash
cd /home/labex/project
if grep -q "validate_attributes" structure.py \
  && grep -q "isinstance" structure.py \
  && grep -q "Validator" structure.py \
  && grep -q "@validate_attributes" stock.py; then
  exit 0
else
  exit 1
fi
