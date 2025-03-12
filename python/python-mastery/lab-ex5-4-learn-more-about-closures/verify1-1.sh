#!/bin/bash
if [ ! -f /home/labex/project/counter.py ]; then
  echo "counter.py file not found"
  exit 1
fi

if ! grep -q "def counter" /home/labex/project/counter.py; then
  echo "counter function not found in counter.py"
  exit 1
fi

if ! grep -q "nonlocal value" /home/labex/project/counter.py; then
  echo "nonlocal statement not found in counter.py"
  exit 1
fi

if ! grep -q "return incr, decr" /home/labex/project/counter.py; then
  echo "Function should return incr and decr functions"
  exit 1
fi

exit 0
