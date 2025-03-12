#!/bin/bash
cd /home/labex/project
if grep -q "def enforce" validate.py && grep -q "type_specs" validate.py && grep -q "return_" validate.py; then
  exit 0
else
  exit 1
fi
