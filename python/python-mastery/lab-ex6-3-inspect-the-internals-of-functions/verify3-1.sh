#!/bin/bash

# Check if the structure.py file contains the required implementations
if grep -q "@classmethod" /home/labex/project/structure.py \
  && grep -q "set_fields" /home/labex/project/structure.py \
  && grep -q "Stock" /home/labex/project/structure.py \
  && grep -q "inspect.signature" /home/labex/project/structure.py; then
  exit 0
else
  exit 1
fi
