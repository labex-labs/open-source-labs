#!/bin/bash

cd /home/labex/project
if grep -q "@shares.setter" stock.py && grep -q "raise TypeError" stock.py && grep -q "raise ValueError" stock.py; then
  exit 0
else
  exit 1
fi
