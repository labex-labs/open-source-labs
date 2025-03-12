#!/bin/bash

cd /home/labex/project
if grep -q "@property" stock.py && ! grep -q "def cost(self):" stock.py; then
  exit 0
else
  exit 1
fi
