#!/bin/bash
grep -q "__set__" /home/labex/project/validate.py \
  && grep -q "PositiveInteger" /home/labex/project/validate.py \
  && grep -q "String" /home/labex/project/validate.py
if [ $? -eq 0 ]; then
  exit 0
else
  echo "Validator classes do not contain required methods or classes"
  exit 1
fi
