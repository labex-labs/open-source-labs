#!/bin/bash
grep -q "from structure import" /home/labex/project/stock.py \
  && grep -q "class Stock" /home/labex/project/stock.py \
  && grep -q "@property" /home/labex/project/stock.py \
  && grep -q "sell" /home/labex/project/stock.py
