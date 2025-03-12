#!/bin/bash
if [ -f ~/project/decimal_stock.py ] && grep -q "class DStock" ~/project/decimal_stock.py && grep -q "from decimal import Decimal" ~/project/decimal_stock.py; then
  exit 0
else
  exit 1
fi
