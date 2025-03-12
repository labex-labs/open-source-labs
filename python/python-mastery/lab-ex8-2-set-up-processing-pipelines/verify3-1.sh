#!/bin/bash
if [ ! -f "/home/labex/project/ticker.py" ]; then
  echo "ticker.py file not found"
  exit 1
fi

if grep -q "from tableformat import create_formatter" "/home/labex/project/ticker.py" \
  && grep -q "formatter = create_formatter" "/home/labex/project/ticker.py" \
  && grep -q "negative = (rec for rec in records if rec.change < 0)" "/home/labex/project/ticker.py" \
  && grep -q "print_table" "/home/labex/project/ticker.py"; then
  exit 0
else
  echo "ticker.py doesn't contain the required pipeline updates"
  exit 1
fi
