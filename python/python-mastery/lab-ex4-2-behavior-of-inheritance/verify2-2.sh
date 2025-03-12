#!/bin/bash

if grep -q "class Validator" /home/labex/project/validate.py \
  && grep -q "class Typed" /home/labex/project/validate.py \
  && grep -q "class Integer" /home/labex/project/validate.py \
  && grep -q "class PositiveInteger" /home/labex/project/validate.py; then
  exit 0
else
  exit 1
fi
