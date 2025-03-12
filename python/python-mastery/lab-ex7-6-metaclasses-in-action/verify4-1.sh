#!/bin/bash
# Check if stock.py exists and contains the right content
grep -q "class Stock" /home/labex/project/stock.py && grep -q "def sell" /home/labex/project/stock.py
exit $?
