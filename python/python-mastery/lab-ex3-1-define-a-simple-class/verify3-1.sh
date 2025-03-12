#!/bin/bash
cd /home/labex/project
if grep -q "def print_portfolio" stock.py && grep -q "print" stock.py && grep -q "for" stock.py; then
  exit 0
else
  exit 1
fi
