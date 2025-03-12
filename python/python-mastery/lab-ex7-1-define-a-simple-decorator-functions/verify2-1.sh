#!/bin/bash
if ! grep -q "def validated" /home/labex/project/validate.py; then
  echo "validated decorator function not found in validate.py"
  exit 1
fi
if ! grep -q "inspect.signature" /home/labex/project/validate.py; then
  echo "inspect.signature not found in validate.py"
  exit 1
fi
if ! grep -q "functools.wraps" /home/labex/project/validate.py; then
  echo "functools.wraps not found in validate.py"
  exit 1
fi
exit 0
