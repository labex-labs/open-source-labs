#!/bin/bash
grep -q "class Stock" /home/labex/project/stock.py \
  && grep -q "def __init__" /home/labex/project/stock.py \
  && grep -q "def cost" /home/labex/project/stock.py || exit 1
