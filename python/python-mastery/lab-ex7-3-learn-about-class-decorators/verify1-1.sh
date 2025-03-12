#!/bin/bash
cd /home/labex/project
if grep -q "name = String()" stock.py \
  && grep -q "shares = PositiveInteger()" stock.py \
  && grep -q "price = PositiveFloat()" stock.py \
  && grep -q "_fields" stock.py \
  && grep -q "create_init" stock.py; then
  exit 0
else
  exit 1
fi
