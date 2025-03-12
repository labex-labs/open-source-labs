#!/bin/bash
cd /home/labex/project
if grep -q "callable" structure.py \
  && grep -q "__annotations__" structure.py \
  && grep -q "nshares: PositiveInteger" stock.py; then
  exit 0
else
  exit 1
fi
