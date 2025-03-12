#!/bin/bash
if [ ! -f "/home/labex/project/ticker.py" ]; then
  echo "ticker.py file not found"
  exit 1
fi

if grep -q "class Ticker" "/home/labex/project/ticker.py" \
  && grep -q "from structure import" "/home/labex/project/ticker.py" \
  && grep -q "name = String" "/home/labex/project/ticker.py" \
  && grep -q "records = (Ticker.from_row" "/home/labex/project/ticker.py"; then
  exit 0
else
  echo "ticker.py doesn't contain the required Ticker class implementation"
  exit 1
fi
