#!/bin/bash

if grep -q "from validate import" /home/labex/project/stock.py \
  && grep -q "PositiveInteger.check" /home/labex/project/stock.py \
  && grep -q "PositiveFloat.check" /home/labex/project/stock.py; then
  exit 0
else
  exit 1
fi
