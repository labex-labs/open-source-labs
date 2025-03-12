#!/bin/bash
if [ -f ~/project/test_stock.py ] && grep -q "from stock import Stock" ~/project/test_stock.py; then
  exit 0
else
  exit 1
fi
