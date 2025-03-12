#!/bin/bash
cd /home/labex/project
if grep -q "def read_portfolio" stock.py && grep -q "open" stock.py && grep -q "append" stock.py; then
  exit 0
else
  exit 1
fi
