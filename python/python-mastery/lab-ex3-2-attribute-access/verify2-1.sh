#!/bin/bash
if grep -q "getattr" /home/labex/.python_history && grep -q "read_portfolio" /home/labex/.python_history; then
  exit 0
else
  exit 1
fi
