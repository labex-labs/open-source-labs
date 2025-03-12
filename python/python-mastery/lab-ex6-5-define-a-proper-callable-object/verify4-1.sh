#!/bin/bash
if [ -f /home/labex/project/stock.py ]; then
  grep -q "ValidatedMethod" /home/labex/project/stock.py \
    && echo "Great! You've implemented the Stock class with ValidatedMethod."
else
  echo "The stock.py file is missing."
fi
