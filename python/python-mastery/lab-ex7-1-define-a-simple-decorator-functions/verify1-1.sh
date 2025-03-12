#!/bin/bash
if [ ! -f /home/labex/project/logcall.py ]; then
  echo "logcall.py file not found"
  exit 1
fi
if ! grep -q "def logged" /home/labex/project/logcall.py; then
  echo "logged function not found in logcall.py"
  exit 1
fi
if ! grep -q "wrapper" /home/labex/project/logcall.py; then
  echo "wrapper function not found in logcall.py"
  exit 1
fi
exit 0
