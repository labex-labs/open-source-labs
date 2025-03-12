#!/bin/bash
cd /home/labex/project
if grep -q "def sell" stock.py && grep -q "self.shares" stock.py; then
  exit 0
else
  exit 1
fi
